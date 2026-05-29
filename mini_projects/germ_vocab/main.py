import os
from helpers import add_word, show_words, update_vocab, read_vocab


if os.path.exists("py-course-2/mini_projects/germ_vocab/vocabluary.json"):
    vocab = read_vocab()
else:
    vocab = {}
        
while True:
    print('      Menu')
    print("1 — Добавить новое слово")
    print("2 — Показать словарь")
    print("3 — Выйти")
    
    user_choice = input("Выберите действие: ")
    
    if user_choice == '1':
        original = input("Введите слово на немецком: ")
        translation = input("Введите слово на укр: ")
        vocab = add_word(vocab, original, translation)
    elif user_choice == "2":
        show_words(vocab)
    elif user_choice == '3':
        print("Сохраняем...")
        update_vocab(vocab=vocab)
        print("Выход из програмы...")
        break   
    else:
        print("Неверная команда!")
        

# 1) .strftime() или String Format Time нужен чтобы обьект модуля datetime сделать строку 
# 2) Это будет другой код формата и собственно будет другое отображение

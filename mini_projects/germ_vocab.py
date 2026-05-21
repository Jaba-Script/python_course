def add_word(dictionary, original, translation):
    dictionary[f'{original}'] = translation
    print("Слова добавлено!")
    return dictionary


def show_words(dictionary):
    print(f"")
    print(f"      Словарь")
    print(f"Немецкий - Украинський")
    for key, value in dictionary.items():
        print(f"|  {key} - {value}")
        
        
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
        print("Выход из програмы...")
        break   
    else:
        print("Неверная команда!")
        

# 1) оно возвращает значение, если не будет то функция автоматически вернет None
# 2) в скобках при def мы обозначаем переменные с которыми будем работать в функцие, при визове ми "ложем" значение в функцию
# 3) нет
import json
import os
from datetime import datetime

def add_word(dictionary, original, translation):
    now_date = datetime.now() 
    dictionary[original] = {
        "translation": translation,
        "add_date": now_date.strftime("%d.%m.%Y %H:%M")
    }
    
    print("Слова добавлено!")
    return dictionary


def show_words(dictionary):
    print(f"")
    print(f"      Словарь")
    print(f"Немецкий - Украинський")
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(f"|  {key} - {value["translation"]}       {value["add_date"]}")
        else:
            print(f"|  {key} - {value}")

                
        

def update_vocab(vocab):
    with open("py-course-2/mini_projects/vocabluary.json", "w", encoding="utf-8") as file:
        json.dump(vocab, file, ensure_ascii=False, indent=4)
        

def read_vocab():
    with open("py-course-2/mini_projects/vocabluary.json", "r", encoding="utf-8") as file:
        return json.load(file)
        


if os.path.exists("py-course-2/mini_projects/vocabluary.json"):
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

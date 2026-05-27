import json
import os

def add_word(dictionary, original, translation):
    dictionary[original] = translation
    print("Слова добавлено!")
    return dictionary


def show_words(dictionary):
    print(f"")
    print(f"      Словарь")
    print(f"Немецкий - Украинський")
    for key, value in dictionary.items():
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
        

# 1) чтобы компютер мог понимать другие языки (символы)
# 2) w - пишет заново, а - дополняет файл
# 3) будет ошыбка FileNotFoundError
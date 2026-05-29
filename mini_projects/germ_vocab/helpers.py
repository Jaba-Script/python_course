import json
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
    with open("py-course-2/mini_projects/germ_vocab/vocabluary.json", "w", encoding="utf-8") as file:
        json.dump(vocab, file, ensure_ascii=False, indent=4)
        

def read_vocab():
    with open("py-course-2/mini_projects/germ_vocab/vocabluary.json", "r", encoding="utf-8") as file:
        return json.load(file)
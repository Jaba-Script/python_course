contacts =[]

while True:
    print("1 — Показать все контакты")
    print("2 — Добавить новый контакт")
    print("3 — Удалить контакт")
    print("4 — Выйти")
    
    user_choice = input("Выберите действие: ")
    
    if user_choice == '1':
        if len(contacts) == 0:
            print("Список пуст!")
        else:
            for contact in contacts:
                print(f"  |  {contact['name']} -- {contact['number']}")  
    elif user_choice == '2':
        print("Введите данные")
        
        new_contact = {}
        new_contact['name'] = input("- Введите имя: ")
        new_contact['number'] = input("- Введите номер: ")
        
        while True:
            agree = input("Подтвердить?(y/n) - ")
            if agree == 'y':
                contacts.append(new_contact)
                print("Контакт создан!")
                break
            elif agree == 'n':
                print("Создание контакта отменено!")
                break
            else:
                print("Неверная команда!")
    elif user_choice == '3':
        delete_contact = input("Введите имя: ")
        for contact in contacts:
            if delete_contact == contact['name']:
                contacts.remove(contact)
                print("Контакт удален!")
    elif user_choice == '4':
        print("Выход из програмы...")
        break   
    else:
        print("Неверная команда!")


            
        
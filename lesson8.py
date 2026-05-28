def book_table():
    while True:
        try:
            guest_num = int(input("Введите число гостей: "))
            break
        except ValueError:
            print("Введите число!")
    return guest_num

print(f"Забронирован столик на {book_table()} гостей")

#1) Выполниться код в exept а потом все продолжится как обычно
#2) exept будет вылавливать все ошыбки. Это плохо потому что под разные ошибки пользователю надо давать разные подсказки
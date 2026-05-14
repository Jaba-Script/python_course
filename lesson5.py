tasks = []
user_data = ""

while user_data != "Стоп":
    user_data = input("Введите задачу: ")
    if user_data != "Стоп" and user_data != "":
        tasks.append(user_data)

# for i in range(3):
#     task = input("Введите задачу: ")

for task in tasks:
    print(f"Дело №{tasks.index(task) + 1}: {task}")
    
# 1) Перебирает целые числа до 5 
# 2) for выполняеться определеное количество раз, а while пока условие правдиво
# 3) Ctrl + C
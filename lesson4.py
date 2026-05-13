shopping_list =[]
print("Введите названия товаров:")

shopping_list.append(input())
shopping_list.append(input())
shopping_list.append(input())

print(f"Ваш список покупок {shopping_list}")
print(f"Первый товар в списке: {shopping_list[0]}")
print(f"Последний товар в списке: {shopping_list[-1]}")

# 1) 0
# 2) .append()
# 3) будет ошыбка IndexError: list index out of range
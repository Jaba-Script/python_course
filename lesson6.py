profile = {}

profile["name"] = input("Введите имя: ")
profile["age"] = input("Введите возраст: ")
profile["city"] = input("Введите город: ")
profile["status"] = "Student"

print(f"Профиль создан: Пользователю {profile['name']} из города {profile['city']} сейчас {profile['age']} лет.")
print(profile.keys())

# 1) да, значение просто перезапишеться
# 2) надо написать ключ в квадратных скобках
# 3) в словаре вместо индекса ключи
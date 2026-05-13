bill_sum = float(input("Счет: "))
tips_percent = float(input("Чаевые: "))
tips_sum = (bill_sum * tips_percent) / 100
print(f"Сумма чаевых: {tips_sum} грн.")

# 1) Нужно использивать функцию float()
# 2) Будет ошибка ValueError
# 3) Получилось сделать 
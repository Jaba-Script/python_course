price = float(input())

if price > 10000:
    discount = 20
elif price > 5000:
    discount = 10
elif price <= 5000:
    discount = 0
    
bill = price * (1 - discount / 100)

if discount > 0:
    print(f"Ваша скидка {discount}%! К оплате: {bill}")
else:
    print(f"Скидки нет. К оплате: {bill}")


# "=" для присваивания значений, а "==" для сравнения
# для позначення кода что входит в if
# elif используют когда нужна дополнительная проверка
    
    
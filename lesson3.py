price = float(input())

if price > 5000:
    discount = 10
    bill = price - ((price * discount) / 100)
    print(f"Ваша скидка {discount}%! К оплате: {bill}")
elif price > 10000:
    discount = 20
    bill = price - ((price * discount) / 100)
    print(f"Ваша скидка {discount}%! К оплате: {bill}")
elif price <= 5000:
    discount = 0
    bill = price - ((price * discount) / 100)
    print(f"Скидки нет. К оплате: {bill}")
    

# "=" для присваивания значений, а "==" для сравнения
# для позначення кода что входит в if
# elif используют когда нужна дополнительная проверка
    
    
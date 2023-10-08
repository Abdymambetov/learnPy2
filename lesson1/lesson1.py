
# result = []

# while True:
#     user = int(input('number '))
#     if user == 0:
#         break
#     else: 
#         result.append(user)

# print(result)


current_money = 2350

products = {
    '1111': ['Яблоко', 50],
    '2222': ['Арбуз', 80],
    '3333': ['Дыня', 90]
}

user = input('Введите код товара')

price = products[user][1]
name = products[user][0]
print(f'Вы купили {name} за {price}')

current_money += price
print(f'На кассе {current_money} сом')
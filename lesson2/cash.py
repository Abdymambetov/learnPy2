class Balance:
    def __init__(self, fileName):
        self.fileName = fileName
        self.current_money = self.readBalance()

    def readBalance(self):
        try:
            with open(self.fileName, 'r+', encoding='UTF_8') as file:
                balance = file.read()
                print(type(balance), balance)
                if balance:
                    return int(balance)
                else: 
                    file.write('0')
                    return 0
        except (FileNotFoundError, IOError):
            with open(self.fileName, 'w+') as cm_file:
                cm_file.write('0')
                return 0
            
    def writeBalance(self):
        with open(self.fileName, 'w+') as cm_file:
            cm_file.write(str(self.current_money))

    def cash_collection(self, amount):
        self.current_money += amount
        self.writeBalance()

    def __str__(self) -> str:
        return f"Текущий баланс {self.current_money} сом"



#База данных
# with open('file.txt', 'r+', encoding='UTF_8') as file:
#     balance = file.read()
#     print(type(balance), balance)
#     if balance:
#         current_money = int(balance)
#     else: 
#         file.write('0')
#         current_money= 0

# def writeBalance(money):
#     with open('file.txt', 'w+') as cm_file:
#         cm_file.write(str(money))

class Products:
    def __init__(self, name, price, packed_date):
        self.name = name
        self.price = price
        self.packed_date = packed_date

    # def display_info(self):
    #     print("product:", self.name, "\npacked_date:", self.packed_date, "\nprice:", self.price, "\nday:", self.day)

    # def show_exp_date(self):
    #     start_day = int(self.packed_date[:2])
    #     start_day += self.day
    #     exp_date = f'{start_day}{self.packed_date[2:]}'
    #     print("expiration date: ", exp_date)

buys = []
products = {
    '1111': Products('Milk', 50, '01.01.2023'),
    '2222': Products('Apple', 20, '10.01.2023'),
    '3333': Products('Chees', 40, '20.01.2023')
}
balance = Balance("file.txt")
while True:
    #пробить товар
    sh_code = input('Введите штих код товара')
    if sh_code == '0':
        print('Смена окончена')
        print(buys)
        print(balance)
        break


    #Сравнить цену
    if sh_code in products:
        price = products[sh_code].price
        name = products[sh_code].name
        buys.append(products[sh_code])
        print(f"Вы купили {name} за {price} сом")
        balance.cash_collection(price)
        print(balance)
    else:
        print("Товар не найден. Пожалуйста, введите корректный штрих-код.")
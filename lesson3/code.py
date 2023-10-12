# class Balance:
#     current_money = 0
#     def __init__(self, fileName):
#         self.fileName = fileName
#         self.get_balance()
#         print('Объект создан', self)
    
#     def __str__(self) -> str:
#         return f'Текущий баланс {self.current_money}'

#     def get_balance(self):
#         try:
#             with open(self.fileName, 'r+', encoding='UTF-8') as cm_file:
#                 balance = cm_file.read()
#             if balance:
#                 self.current_money += int(balance)
#             else:
#                 cm_file.write('0')
#                 self.current_money = 0
#         except FileNotFoundError:
#             with open(self.fileName, 'w+') as cm_file:
#                 cm_file.write('0')
#                 self.current_money = 0

#         self.current_money = self.current_money

#     def add_money(self, money):
#         self.current_money += money
#         self.write_balance()
#         print(f"Добавление баланса {money}", self)
#     def write_balance(self):
#         with open(self.fileName, 'w+') as cm_file:
#             cm_file.write(str(self.current_money))

#     def incasation(self):
#         if self.current_money > 0:
#             print(f'Инкасация {self.current_money}', self)
#             self.current_money = 0
#         else:
#             print('Инкасация невозможна, касса пуста',self)
#         print(self)

# b1 = Balance('test.txt')
# b1.add_money(100)
# b1.add_money(50)
# b1.incasation()
# b1.incasation()

# b2 = Balance('file1.txt')
# b2.add_money(100)
# b2.incasation()



# from my_lib import my_sum
# from mypackage import myclass
# from mypackage.myclass import *
# from mypackage.myclass import Battle_lord, a
# import mypackage
from mypackage import *
b = Battle_lord()
print(b.volume)
# print(my_sum(2, 2))
print(a)


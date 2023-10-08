class Balanse():
    def __init__(self, money):
        self.current_balance = money
        self.exemple = True

    current_balance = 0

    def add_money(self, money):
        self.current_balance += money

class DayBalance(Balanse):
    def __init__(self, money, day):
        super().__init__(money)
        self.day = day
    day = '01.01.2023'

class Valuta:
    def set_valuta(self, type):
        self.type = type

class DayBalanceValuta(DayBalance, Valuta):
    def __init__(self, money, day, valute_type):
        super().__init__(money, day)
        self.set_valuta(valute_type)
    def show_them(self):
        print(f'{self.current_balance} {self.type} {self.day}')

    def incasation(self):
        if self.current_balance >0:
            print(f'Инкассация{self.current_balance} {self.type} {self.day}')
            self.current_balance = 0
        else:
            print('Инкасация невозможна, касса пуста')


cash1 = DayBalanceValuta(1500, '06.10.2023', 'som')
cash1.show_them()
cash1.incasation()

cash2 = DayBalanceValuta(20000, '20.10.2023', '$')
cash2.show_them()
cash2.incasation()
cash2.incasation()
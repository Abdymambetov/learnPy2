
class Products:
    def __init__(self, name, price, packed_date, day):
        self.name = name
        self.price = price
        self.packed_date = packed_date
        self.day = day

    # def display_info(self):
    #     print("product:", self.name, "\npacked_date:", self.packed_date, "\nprice:", self.price, "\nday:", self.day)

    def __str__(self) -> str:
        print(f'product:', self.name, '\npacked_date:', self.packed_date, '\nprice:', self.price, '\nday:', self.day)
    
    def show_exp_date(self):
        start_day = int(self.packed_date[:2])
        start_day += self.day
        exp_date = f'{start_day}{self.packed_date[2:]}'
        print(f'expiration date: {exp_date}')


product1 = Products('milk', 50, "01.01.2023", 15)
# product1.display_info()
product1.show_exp_date()
print(product1)
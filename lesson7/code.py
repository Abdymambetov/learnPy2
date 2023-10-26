from openpyxl import Workbook

name = input('What? ')

class MyExcel(Workbook):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)
        self.use_first_page()
        self.save(name)
    
    def use_first_page(self):
        self.first_page = self[self.sheetnames[0]]
    
    def write_in_cell(self, cell: str, value):
        self.first_page[cell] = value
        self.save(self.name)


my_excel2 = MyExcel('names.xlsx')
my_excel2.write_in_cell('A2', name)


# excelBook = Workbook()
# page = excelBook.active
# page['A1'] = name
# excelBook.save('names.xlsx')
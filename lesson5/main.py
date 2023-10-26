from openpyxl import Workbook, load_workbook

class MyExcel(Workbook):
    special_name = 'report.xlsx'

e1 = MyExcel()
e1.save(e1.special_name)

file_name = "exemple_1.xlsx"
excel_file = load_workbook(file_name)
page = excel_file['Sheet']
page['C7'] = 4
excel_file.save(file_name)

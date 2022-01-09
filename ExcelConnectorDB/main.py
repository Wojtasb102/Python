from openpyxl import *
import os


class Connector:
    def __init__(self, excelName):
        self.excelName = excelName
        if not self.is_file():
            workbook = Workbook()
            workbook.save(filename=excelName)
        self.workbook = load_workbook(filename=self.excelName)
        self.worksheet = self.workbook.active

    def is_file(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, self.excelName)
        print(os.path.isfile(filename))
        return os.path.isfile(filename)

    def sheet_list(self):
        return self.workbook.sheetnames

    def read_cell(self, x, y):
#        return self.worksheet.cell(row=x, column=y).number_format
        return self.worksheet.cell(row=x, column=y).value

    def change_worksheet(self, sheetname):
        self.worksheet = self.workbook[sheetname]


def main():
    print("Start Main")
    conector = Connector("Excel.xlsx")
    conector.is_file()
    print("Start Main")
    print(conector.sheet_list())
    conector.change_worksheet("Sheet")
    print(conector.read_cell( 1, 1))
    conector.change_worksheet("Arkusz1")
    print(conector.read_cell(1, 1))


main()

from openpyxl import *
import os
import sqlite3


class Connector:
    def __init__(self, excelName, dbName):
        self.excelName = excelName
        self.dbName = dbName
        self.dirname = os.path.dirname(__file__)
        if not self.is_file(self.excelName):
            workbook = Workbook()
            workbook.save(filename=excelName)
        self.workbook = load_workbook(filename=self.excelName)
        self.worksheet = self.workbook.active
        if not self.is_file(self.dbName):
            filename = os.path.join(self.dirname, self.dbName)
            conn = sqlite3.connect(filename)

    def is_file(self, fileName):
        #dirname = os.path.dirname(__file__)
        filename = os.path.join(self.dirname, fileName)
        print(os.path.isfile(filename))
        return os.path.isfile(filename)

    def sheet_list(self):
        return self.workbook.sheetnames

    def read_cell(self, x, y):
#        return self.worksheet.cell(row=x, column=y).number_format
        return self.worksheet.cell(row=x, column=y).value

    def change_worksheet(self, sheetname):
        self.worksheet = self.workbook[sheetname]

    def create_db_connection(self):
        filename = os.path.join(self.dirname, self.dbName)
        conn = sqlite3.connect(filename)



def main():
    print("Start Main")
    conector = Connector("Excel.xlsx", "Database.db")
    conector.is_file("Excel.xlsx")
    conector.is_file("Database.db")
    print("Start Main")
    print(conector.sheet_list())
    conector.change_worksheet("Sheet")
    print(conector.read_cell( 1, 1))
    conector.change_worksheet("Arkusz1")
    print(conector.read_cell(1, 1))

main()

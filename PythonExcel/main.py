import datetime
from excel import *
from sql import *


# mycursor.execute("SELECT * FROM `przyjecia` ")

# def load_from_xlsx_to_sql():
def cell_to_data(data):
    return str(data)[0:10]


def load_worksheet_to_db(worksheet):
    ws = wb.Worksheets(worksheet)
    mycursor.execute("TRUNCATE TABLE {}".format(worksheet))
    lastRow = ws.UsedRange.Rows.Count
    # print(lastRow)

    for i in range(2, lastRow + 1):
        name = ws.Cells(i, 2)
        data = cell_to_data(ws.Cells(i, 3))
        dep = ws.Cells(i, 4)
        # print("INSERT INTO {} (IMIE, DATA, DZIAL) VALUES ('{}', '{}', {})".format(worksheet, name, data[0:10], dep))
        mycursor.execute(
            "INSERT INTO {} (IMIE, DATA, DZIAL) VALUES ('{}', '{}', '{}')".format(worksheet, name, data[0:10], dep))
        mydb.commit()


def get_record_number():
    wykaz = wb.Worksheets("wykaz")
    lastRow = wykaz.UsedRange.Rows.Count + 1
    # print(lastRow)
    row = 2;
    for dzial in ("P1", "P2"):
        for i in range(2, lastRow):
            data = cell_to_data(wykaz.Cells(i, 1))
            # print(data)
            mycursor.execute("SELECT COUNT(*) FROM przyjecia WHERE DZIAL = '{}' AND DATA = '{}';".format(dzial, data))
            myresult = mycursor.fetchone()
            wykaz.Cells(i, row).value = myresult[0]
            # print(myresult[0])
        row = row + 1


xl = Dispatch('Excel.Application')
wb = xl.Workbooks.Open(DIR + "\my_sheet.xlsx")

xl.Visible = True

load_worksheet_to_db("przyjecia")
load_worksheet_to_db("odejscia")

ws = wb.Worksheets("przeniesienia")
mycursor.execute("TRUNCATE TABLE {}".format("przeniesienia"))
lastRow = ws.UsedRange.Rows.Count
# print(lastRow)

for i in range(2, lastRow + 1):
    name = ws.Cells(i, 2)
    data = cell_to_data(ws.Cells(i, 3))
    dep_to = ws.Cells(i, 4)
    dep_from = ws.Cells(i, 5)
    # print("INSERT INTO {} (IMIE, DATA, DZIAL) VALUES ('{}', '{}', {})".format(worksheet, name, data[0:10], dep))
    mycursor.execute(
        "INSERT INTO przeniesienia (IMIE, DATA, DZIALDO, DZIALZ) VALUES ('{}', '{}', '{}', '{}')".format(name,
                                                                                                         data[0:10],
                                                                                                         dep_to,
                                                                                                         dep_from))
    mydb.commit()

get_record_number()
wykaz = wb.Worksheets("wykaz")
lastRow = wykaz.UsedRange.Rows.Count + 1
# print(lastRow)
row = 2;
for dzial in ("P1", "P2"):
    for i in range(2, lastRow):
        data = cell_to_data(wykaz.Cells(i, 1))
        # print(data)
        mycursor.execute("SELECT COUNT(*) FROM odejscia WHERE DZIAL = '{}' AND DATA = '{}';".format(dzial, data))
        myresult = mycursor.fetchone()
        wykaz.Cells(i, row).value -= myresult[0]
        # print(myresult[0])
    row = row + 1

row = 2;
for dzial in ("P1", "P2"):
    for i in range(2, lastRow):
        data = cell_to_data(wykaz.Cells(i, 1))
        # print(data)
        mycursor.execute("SELECT COUNT(*) FROM przeniesienia WHERE DZIALDO = '{}' AND DATA = '{}';".format(dzial, data))
        myresult = mycursor.fetchone()
        wykaz.Cells(i, row).value += myresult[0]
        mycursor.execute("SELECT COUNT(*) FROM przeniesienia WHERE DZIALZ = '{}' AND DATA = '{}';".format(dzial, data))
        myresult = mycursor.fetchone()
        wykaz.Cells(i, row).value -= myresult[0]
        # print(myresult[0])
    row = row + 1

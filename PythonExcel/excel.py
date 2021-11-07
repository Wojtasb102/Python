from win32com.client import Dispatch
import sql
import os

DIR = os.getcwd()
print(DIR)

print(DIR+"tekst")
def put_data_to_worksheet(xpos, ypos, worksheet, data):
    if (xpos > 0) and (ypos > 0):
        for x in range(len(data)):
            for y in range(len(data[x])):
                cell = worksheet.Cells(x + xpos, y + ypos)
                cell.Value = data[x][y]
    else:
        print("Zła pozycja początkowa")


def open_elsx(dir, name, sheet):
    xl = Dispatch('Excel.Application')
    # wb = xl.Workbooks.Add()
    # ws = wb.Worksheets.Add()
    wb = xl.Workbooks.Open(dir+name)
    ws = wb.Worksheets(sheet)
    xl.Visible = True
    return ws


#ws = open_elsx(dir=DIR, name="\my_sheet.xlsx",sheet="Arkusz1")
#cell_value = ws.Cells(3)
#cell = ws.Cells(5, 2)
#cell.Value = repr(sql.fetch_from_sql())
#print(cell_value)

#put_data_to_worksheet(4, 4, ws, sql.fetch_from_sql())

# wb.Close(True, r'C:\Users\wbachinski\Documents\GitHub\Python\PythonExcel\my_sheet.xlsx')

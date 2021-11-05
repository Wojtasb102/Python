from win32com.client import Dispatch
import sql


def open_elsx (dir, name, sheet):
    xl = Dispatch('Excel.Application')
    # wb = xl.Workbooks.Add()
    # ws = wb.Worksheets.Add()
    wb = xl.Workbooks.Open(r'C:\Users\wbachinski\Documents\GitHub\Python\PythonExcel\my_sheet.xlsx')
    ws = wb.Worksheets("Arkusz1")
    xl.Visible = True
    return ws


ws = open_elsx(dir = "", name= r'C:\Users\wbachinski\Documents\GitHub\Python\PythonExcel\my_sheet.xlsx', sheet="Arkusz1")
cell_value = ws.Cells(3)
cell = ws.Cells(2)
cell.Value = repr(sql.fetch_from_sql())
print(cell_value)
#wb.Close(True, r'C:\Users\wbachinski\Documents\GitHub\Python\PythonExcel\my_sheet.xlsx')
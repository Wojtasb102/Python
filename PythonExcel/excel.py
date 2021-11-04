from win32com.client import Dispatch
xl = Dispatch('Excel.Application')
#wb = xl.Workbooks.Add()
#ws = wb.Worksheets.Add()
wb = xl.Workbooks.Open(r'C:\Users\wbachinski\Documents\GitHub\Python\PythonExcel\my_sheet.xlsx')
ws = wb.Worksheets("Arkusz1")
xl.Visible = True
cell = ws.Cells(2)
cell.Value = 'Some text'
#wb.Close(True, r'C:\Users\wbachinski\Documents\GitHub\Python\PythonExcel\my_sheet.xlsx')
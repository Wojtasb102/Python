

#now = datetime.datetime(2009, 5, 5)
#str_now = now.date().isoformat()
#print("INSERT INTO {} (IMIE, DATA, DZIAL) VALUES ({}, {}, {})".format("przyjecia", "'MARCIN BAK'", str_now, "'P1'"))


#mycursor.execute("TRUNCATE TABLE przyjecia")
#mycursor.execute(
#    "INSERT INTO {} (IMIE, DATA, DZIAL) VALUES ({}, '{}', {})".format("przyjecia", "'MARCIN BAK'", str_now, "'P1'"))
#mydb.commit()

#mycursor.execute("SELECT * FROM `przyjecia`")
#myresult = mycursor.fetchall()
#print(myresult)
# wb = xl.Workbooks.Add()
# ws = wb.Worksheets.Add()
# wykaz = open_elsx(dir=DIR, name="\my_sheet.xlsx", sheet="wykaz")
# cell_value = ws.Cells(2, 2)

# dlaczego tak? nie wiem...  https://docs.microsoft.com/pl-pl/office/vba/api/excel.xldirection
# https://docs.microsoft.com/pl-pl/office/vba/api/Excel.Range.End
# xlUp = -4162
# lastrow: int = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
# print(lastrow)

# cell = ws.Cells(2, 2)
# cell.Value = repr(sql.fetch_from_sql())
# print(cell_value)

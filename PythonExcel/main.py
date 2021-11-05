import sql
#from sql import *

#data = sql.fetch_from_sql()
sql.send_query("SELECT * FROM wykaz")
sql.send_query("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'wykaz'")
sql.send_query("SHOW COLUMNS FROM 34017600_wykaz.wykaz")
sql.send_query("SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('wykaz')")
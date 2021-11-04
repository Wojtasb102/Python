import mysql.connector


mydb = mysql.connector.connect(
  host="serwer2180298.home.pl",
  user="34017600_wykaz",
  password="k8VPpxzd",
  database="34017600_wykaz"
)



mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM wykaz")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#hasło do bazy ZaQ1@wSx
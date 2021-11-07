import datetime

import mysql.connector



mydb = mysql.connector.connect(
    host="serwer2180298.home.pl",
    user="34017600_wykaz",
    password="k8VPpxzd",
    database="34017600_wykaz"
)
mycursor = mydb.cursor()

def send_query(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(myresult)

def insert_into_table(table_name):
    mycursor = mydb.cursor()


def fetch_from_sql():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM wykaz")
    myresult = mycursor.fetchall()
    nested = []

    print(len(myresult))
    print(len(myresult[1]))

    for x in range(len(myresult)):
        # x = str.strip("()")
        data = []
        for y in range(len(myresult[x])):
            data.append(myresult[x][y])
        nested.append(data)

    print(myresult[1][2])
    return myresult


# hasło do bazy ZaQ1@wSx

#now = datetime.datetime(2009, 5, 5)
#str_now = now.date().isoformat()
#mycursor = mydb.cursor()
#mycursor.execute("INSERT INTO przyjecia (IMIE, DATA, DZIAL) VALUES (%s, %s, %s)", ("MARCIN BAK", str_now, "P1"))
#mydb.commit()
#send_query("SELECT * FROM `przyjecia` ")



# from sql import *

# data = sql.fetch_from_sql()
# sql.send_query("SELECT * FROM wykaz")
# sql.send_query("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'wykaz'")
# sql.send_query("SHOW COLUMNS FROM 34017600_wykaz.wykaz")


# Stworzenie tabeli "przyjecia" z ID IMIE DATA i DZIAl
# sql.send_query("CREATE TABLE przyjecia(ID int, IMIE varchar(30), DATA date, DZIAL varchar(10));")


# cursor.execute("INSERT INTO table (name, id, datecolumn) VALUES (%s, %s, '%s')",
#               ("name", 4, now))

# sql.send_query("INSERT INTO przyjecia (IMIE, DATA, DZIAL) VALUES (%s, '%s', %s)",( "MARCIN BAK", now, "P1"))
# sql.send_query("SELECT * FROM `przyjecia` ")
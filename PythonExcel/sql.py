import mysql.connector

mydb = mysql.connector.connect(
    host="serwer2180298.home.pl",
    user="34017600_wykaz",
    password="k8VPpxzd",
    database="34017600_wykaz"
)


def fetch_from_sql():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM wykaz")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    return myresult
# hasło do bazy ZaQ1@wSx

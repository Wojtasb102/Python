import mysql.connector

mydb = mysql.connector.connect(
    host="serwer2180298.home.pl",
    user="34017600_wykaz",
    password="k8VPpxzd",
    database="34017600_wykaz"
)


def send_query(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(myresult)


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

import sqlite3
conn = sqlite3.connect('C:\\Users\\wbachinski\\Documents\\GitHub\\Python\\ruchyPracownikow\\example.sqlite')
c = conn.cursor()
# Utwórz tabelę
c.execute('''CREATE TABLE transakcje
             (data TEXT, przedmiot_id INTEGER, cena REAL)''')
# Wstaw dane
c.execute("""INSERT INTO transakcje VALUES 
        ('2020-05-06', 36, 17.50)""")
c.execute("""INSERT INTO transakcje VALUES 
        ('2020-05-19', 18, 39.99)""")
# Zapisz zmiany
conn.commit()
# Zamknięcie połączenia z bazą danych
conn.close()
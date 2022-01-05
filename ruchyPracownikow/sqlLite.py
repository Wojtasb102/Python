import sqlite3

PATH = "C:/Users/Marta/Documents/GitHub/Python/ruchyPracownikow/"
conn = sqlite3.connect("{}example.sqlite".format(PATH))
c = conn.cursor()
# Utwórz tabelę
c.execute(
    ''' ''')

# Zapisz zmiany
conn.commit()
# Zamknięcie połączenia z bazą danych
conn.close()

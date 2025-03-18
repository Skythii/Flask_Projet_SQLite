import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (titre) VALUES (?)",('A lécole des sorciers'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('La chambre des secrets'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Le prisonier d'ascaban'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('La coupe de feu'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Lordre du phénix'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Le prince de sang mélé'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Les reliques de la mort'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Nan mais alo quoi'))

connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect('database.db')

with open('schemabb.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (titre, auteur) VALUES (?, ?)",('A lécole des sorciers', 'JK Rowling' ))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('La chambre des secrets', 'JK Rowling'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Le prisonier d'ascaban', 'JK Rowling'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('La coupe de feu', 'JK Rowling'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Lordre du phénix', 'JK Rowling'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Le prince de sang mélé', 'JK Rowling'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Les reliques de la mort', 'JK Rowling'))
cur.execute("INSERT INTO livres (titre) VALUES (?)",('Nan mais alo quoi', 'Thibault Demaret'))

connection.commit()
connection.close()

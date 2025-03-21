import sqlite3

connection = sqlite3.connect('bibliotheque.db')

with open('schemabb.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('A lécole des sorciers', 'JK Rowling', 5 ))
cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('La chambre des secrets', 'JK Rowling', 6))
cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('Le prisonier dascaban', 'JK Rowling', 4))
cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('La coupe de feu', 'JK Rowling', 7))
cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('Lordre du phénix', 'JK Rowling', 3))
cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('Le prince de sang mélé', 'JK Rowling', 9))
cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('Les reliques de la mort', 'JK Rowling', 8))
cur.execute("INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)",('Nan mais alo quoi', 'Thibault Demaret', 10))


cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

connection.commit()
connection.close()

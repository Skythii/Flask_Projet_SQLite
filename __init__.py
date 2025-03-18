from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['authentifie'] = True
            return redirect(url_for('lecture'))
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')

# API Gestion des livres
@app.route('/livres', methods=['POST'])
def ajouter_livre():
    data = request.get_json()
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)', (data['titre'], data['auteur'], data['quantite']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livre ajouté avec succès"}), 201

@app.route('/livres', methods=['GET'])
def afficher_livres():
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres')
    livres = cursor.fetchall()
    conn.close()
    return jsonify(livres)

@app.route('/livres/<int:id>', methods=['GET'])
def afficher_livre(id):
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE id = ?', (id,))
    livre = cursor.fetchone()
    conn.close()
    return jsonify(livre) if livre else (jsonify({"message": "Livre non trouvé"}), 404)

@app.route('/livres/<int:id>', methods=['PUT'])
def modifier_livre(id):
    data = request.get_json()
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE livres SET titre = ?, auteur = ?, quantite = ? WHERE id = ?', (data['titre'], data['auteur'], data['quantite'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livre mis à jour"})

@app.route('/livres/<int:id>', methods=['DELETE'])
def supprimer_livre(id):
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livres WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livre supprimé"})

# API Gestion des utilisateurs
@app.route('/clients', methods=['GET'])
def get_clients():
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()
    conn.close()
    return jsonify(clients)

# API Gestion des emprunts
@app.route('/emprunts', methods=['POST'])
def emprunter_livre():
    data = request.get_json()
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO emprunts (id_client, id_livre) VALUES (?, ?)', (data['id_client'], data['id_livre']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livre emprunté avec succès"}), 201

@app.route('/emprunts/<int:id>', methods=['PUT'])
def retourner_livre(id):
    conn = sqlite3.connect('dbbibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE emprunts SET date_retour = CURRENT_TIMESTAMP WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livre retourné avec succès"})

if __name__ == "__main__":
    app.run(debug=True)

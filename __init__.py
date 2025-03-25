from flask import Flask, render_template, jsonify, request, redirect, url_for, session 
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

# Page d'accueil
@app.route('/', methods=['GET', 'POST'])
def authentification():
    if est_authentifie():  # Si l'utilisateur est déjà authentifié
        return redirect(url_for('accueil'))  # Redirige vers la page d'accueil
    if request.method == 'POST':  # Traitement de la soumission du formulaire
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['authentifie'] = True
            return redirect(url_for('accueil'))  # Redirige vers l'accueil après l'authentification
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

@app.route('/accueil')
def accueil():
    if not est_authentifie():
        return redirect(url_for('authentification'))  # Redirige vers l'authentification si non authentifié
    return render_template('accueil.html')  # Affiche la page d'accueil après authentification


@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('bibliotheque.db')
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
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')

# API Gestion des livres
# Ajouter un livre (formulaire)
@app.route('/ajouter_livre', methods=['GET'])
def ajouter_livre_form():
    return render_template('ajouter_livre.html')

# Ajouter un livre (traitement POST)
@app.route('/livres', methods=['POST'])
def ajouter_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']
    quantite = request.form['quantite']

    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livres (titre, auteur, quantite) VALUES (?, ?, ?)', (titre, auteur, quantite))
    conn.commit()
    conn.close()

    return redirect(url_for('afficher_livres'))

# Afficher les livres
@app.route('/livres', methods=['GET'])
def afficher_livres():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres')
    livres = cursor.fetchall()
    conn.close()
    return render_template('afficher_livres.html', livres=livres)

# Modifier un livre (formulaire)
@app.route('/livres/<int:id>', methods=['GET'])
def modifier_livre_form(id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE id = ?', (id,))
    livre = cursor.fetchone()
    conn.close()
    return render_template('modifier_livre.html', livre=livre)

# Modifier un livre (traitement POST)
@app.route('/livres/<int:id>', methods=['POST'])
def modifier_livre(id):
    titre = request.form['titre']
    auteur = request.form['auteur']
    quantite = request.form['quantite']

    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE livres SET titre = ?, auteur = ?, quantite = ? WHERE id = ?', 
                   (titre, auteur, quantite, id))
    conn.commit()
    conn.close()

    return redirect(url_for('afficher_livres'))

# Supprimer un livre
@app.route('/livres/<int:id>', methods=['GET'])
def supprimer_livre(id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livres WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('afficher_livres'))

# API Gestion des utilisateurs
@app.route('/clients', methods=['GET'])
def get_clients():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()
    conn.close()
    return jsonify(clients)

# API Gestion des emprunts
@app.route('/emprunts', methods=['POST'])
def emprunter_livre():
    data = request.get_json()
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO emprunts (id_client, id_livre) VALUES (?, ?)', (data['id_client'], data['id_livre']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livre emprunté avec succès"}), 201

@app.route('/emprunts/<int:id>', methods=['PUT'])
def retourner_livre(id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE emprunts SET date_retour = CURRENT_TIMESTAMP WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livre retourné avec succès"})

if __name__ == "__main__":
    app.run(debug=True)

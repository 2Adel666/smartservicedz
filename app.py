from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "<h1>Bienvenue sur SmartServiceDZ</h1><p>Accédez au <a href='/formulaire'>formulaire de facture</a>.</p>"

@app.route("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.route("/submit", methods=["POST"])
def recevoir_formulaire():
    data = request.get_json()
    
    print("Données reçues :", data)

    # Tu pourrais ici sauvegarder dans un fichier, base de données, etc.

    return jsonify({"message": "Données reçues avec succès", "status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from services.facture import generer_facture

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/api/generate-invoice', methods=['POST'])
def api_generate_invoice():
    data = request.json
    facture = generer_facture(data['client'], float(data['montant']))
    return jsonify(facture)

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Route pour afficher le formulaire
@app.route("/formulaire", methods=["GET"])
def afficher_formulaire():
    return render_template("formulaire.html")

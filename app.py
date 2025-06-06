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


from flask import Flask, request, jsonify
from flask_cors import CORS
from services.facture import generer_facture
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Bienvenue sur SmartServiceDZ"

@app.route('/facture', methods=['POST'])
def facture():
    data = request.get_json()
    path = generer_facture(data)
    return jsonify({"status": "ok", "message": "Facture générée", "fichier": path})

if __name__ == '__main__':
    os.makedirs("static/factures", exist_ok=True)
    app.run(debug=True)

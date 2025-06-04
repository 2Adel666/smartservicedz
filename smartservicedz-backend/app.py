from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/facture", methods=["POST"])
def facture():
    data = request.get_json()
    print("Données reçues :", data)
    return jsonify({"message": "Formulaire reçu", "status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
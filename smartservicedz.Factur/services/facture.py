
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generer_facture(data):
    numero = data.get("numero", f"FAC-{int(datetime.now().timestamp())}")
    client = data.get("client", "Client inconnu")
    date = data.get("date", datetime.now().strftime("%d/%m/%Y"))
    montant_ht = data.get("montant_ht", 0)
    tva = data.get("tva", 0)
    total = data.get("total", 0)

    nom_fichier = f"facture_{numero}.pdf"
    chemin_fichier = os.path.join("static", "factures", nom_fichier)
    os.makedirs(os.path.dirname(chemin_fichier), exist_ok=True)

    c = canvas.Canvas(chemin_fichier, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, f"Facture : {numero}")
    c.drawString(100, 780, f"Client : {client}")
    c.drawString(100, 760, f"Date : {date}")
    c.drawString(100, 740, f"Montant HT : {montant_ht} DA")
    c.drawString(100, 720, f"TVA : {tva} %")
    c.drawString(100, 700, f"Total TTC : {total} DA")
    c.save()
    return chemin_fichier

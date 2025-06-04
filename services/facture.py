from datetime import datetime

def generer_facture(client, montant):
    ttc = montant * 1.19  # TVA 19%
    return {
        "client": client,
        "montant_ht": montant,
        "tva": 19,
        "total": round(ttc, 2),
        "date": datetime.now().strftime("%d/%m/%Y"),
        "numero": f"FAC-{datetime.now().timestamp()}"
    }

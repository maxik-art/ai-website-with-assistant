
# app.py – Flask-Backend für den AI-Assistenten

from flask import Flask, request, jsonify  # Flask-Basisfunktionen importieren
from flask_cors import CORS  # CORS-Unterstützung für Cross-Origin-Anfragen

app = Flask(__name__)  # Flask-App initialisieren
CORS(app)  # Aktiviert CORS für alle Routen – wichtig für Frontend-Backend-Kommunikation

# Route für die API-Anfrage vom Frontend
@app.route('/ask', methods=['POST'])
def ask():
    # Hole die JSON-Daten aus der Anfrage (enthält die Frage des Users)
    data = request.get_json()
    user_question = data.get('question')  # Extrahiere die Frage

    # Debug-Ausgabe im Terminal (hilfreich beim lokalen Testen)
    print("User asked:", user_question)

    # Beispielantwort – hier könnte die echte AI-Logik integriert werden
    response = f"You asked: {user_question}. (This is a placeholder response.)"

    # JSON-Antwort an das Frontend zurückgeben
    return jsonify({'answer': response})

# Starte die Flask-App
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Läuft lokal auf Port 5000

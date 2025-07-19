# app.py – Flask-Backend für den AI-Assistenten mit OpenAI GPT-Anbindung

from flask import Flask, request, jsonify  # Flask-Basisfunktionen importieren
from flask_cors import CORS  # CORS-Unterstützung für Frontend-Backend-Kommunikation
import openai  # OpenAI SDK für API-Aufrufe

# 🔑 Deinen API-Key hier einfügen
openai.api_key = "sk-proj-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"  # <-- Ersetze mit deinem kopierten API-Key

# Flask-App initialisieren
app = Flask(__name__)
CORS(app)  # Aktiviert CORS für alle Routen

# Route für die API-Anfrage vom Frontend
@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Hole die JSON-Daten aus der Anfrage (enthält die Frage des Users)
        data = request.get_json()
        user_question = data.get('question')  # Extrahiere die Frage
        
        print("User asked:", user_question)  # Debug-Ausgabe im Terminal

        # 🧠 Sende die User-Frage an OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",  # oder "gpt-3.5-turbo" wenn kein GPT-4 verfügbar
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for maxik.ai."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=500,
            temperature=0.7
        )

        # Extrahiere die Antwort des AI-Models
        ai_answer = response['choices'][0]['message']['content'].strip()

        # Debug-Ausgabe
        print("AI answered:", ai_answer)

        # Sende die AI-Antwort an das Frontend zurück
        return jsonify({'answer': ai_answer})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'answer': "❌ Sorry, there was an error processing your request."}), 500

# Starte die Flask-App
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  # Läuft lokal auf Port 5000

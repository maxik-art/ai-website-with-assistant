# app.py – Flask-Backend für den AI-Assistenten mit OpenAI GPT-Anbindung

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# 🏡 Nur lokal .env laden (Render braucht es nicht)
if os.environ.get("RENDER") != "true":
    from dotenv import load_dotenv
    load_dotenv()

# 🔑 API-Key aus Umgebungsvariable holen
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Flask-App initialisieren
app = Flask(__name__)
CORS(app)

# Root-Route (Health Check)
@app.route('/')
def home():
    return "✅ Flask-API läuft! Nutze /ask für den Chatbot."

# Chatbot-API-Endpunkt
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'answer': "❌ No prompt provided."}), 400

    try:
        # OpenAI API Call
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for maxik.ai."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )

        # Extrahiere Antwort
        ai_answer = response['choices'][0]['message']['content'].strip()

        return jsonify({'answer': ai_answer})

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'answer': "❌ Sorry, there was an error processing your request."}), 500

# Lokaler Start
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

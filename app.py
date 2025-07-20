# app.py – Flask-Backend für den AI-Assistenten mit OpenAI GPT-Anbindung

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Nur lokal .env laden (Render braucht es nicht)
if os.environ.get("RENDER") != "true":
    from dotenv import load_dotenv
    load_dotenv()
    
openai.api_key = os.environ.get("OPENAI_API_KEY")

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask-API läuft! Benutze /ask für den Chat."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'answer': "❌ No prompt provided."}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    ai_answer = response['choices'][0]['message']['content'].strip()
    return jsonify({'answer': ai_answer})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

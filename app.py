
from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# OpenAI API Key
openai.api_key = os.environ.get("OPENAI_API_KEY", "your-api-key-here")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask_ai():
    data = request.json
    user_message = data.get("message", "")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )
        ai_reply = response.choices[0].message["content"]
        return jsonify({"reply": ai_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return "✅ AI Assistant is running!"

if __name__ == "__main__":
    app.run(debug=True)

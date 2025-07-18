
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create HTTPX client WITHOUT proxies
http_client = httpx.Client(proxies=None)

app = Flask(__name__)

# Create OpenAI client without proxy
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "your-api-key-here"),
    http_client=http_client
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask_ai():
    data = request.json
    user_message = data.get("message", "")
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )
        ai_reply = response.choices[0].message.content
        return jsonify({"reply": ai_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    try:
        models = client.models.list()
        return jsonify({"status": "ok", "models_count": len(models.data)})
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

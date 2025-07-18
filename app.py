
from flask import Flask, render_template, request, jsonify
from openai import OpenAI, APIError
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create HTTPX client WITHOUT proxies
http_client = httpx.Client(proxies=None)

app = Flask(__name__)

# Create OpenAI client without proxy
api_key = os.environ.get("OPENAI_API_KEY", None)
client = None
if api_key:
    client = OpenAI(
        api_key=api_key,
        http_client=http_client
    )

# Read model from environment or fallback to gpt-3.5-turbo
MODEL_NAME = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask_ai():
    data = request.json
    user_message = data.get("message", "")
    if client:
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": user_message}]
            )
            ai_reply = response.choices[0].message.content
            return jsonify({"reply": ai_reply})
        except APIError as api_error:
            # Handle quota errors or any OpenAI API issues
            print(f"OpenAI API error: {api_error}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    # Demo-Mode Fallback response
    demo_reply = f"(Demo Mode) You asked: '{user_message}'. This is a placeholder response."
    return jsonify({"reply": demo_reply})

@app.route("/health")
def health():
    if client:
        try:
            models = client.models.list()
            return jsonify({
                "status": "ok",
                "models_count": len(models.data),
                "default_model": MODEL_NAME
            })
        except Exception as e:
            return jsonify({"status": "error", "details": str(e)}), 500
    else:
        return jsonify({
            "status": "demo",
            "details": "Running in Demo Mode – OpenAI API not configured or unavailable."
        })

if __name__ == "__main__":
    app.run(debug=True)

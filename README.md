
# AI Website with Assistant (OpenAI v1.x, Model Configurable)

This Flask app uses OpenAI's API (v1.x) and allows model selection via environment variables.

## 🚀 Deployment on Render

1. Create a **New Web Service** on [render.com](https://render.com).
2. Connect this repo.
3. Set environment variables:
   ```
   OPENAI_API_KEY=sk-your-openai-key
   OPENAI_MODEL=gpt-3.5-turbo  # Or gpt-4 if available
   ```
4. Build Command:
   ```
   pip install -r requirements.txt
   ```
5. Start Command:
   ```
   gunicorn app:app
   ```
6. Deploy.

## ✅ Health Check

- Visit `/health` to verify the API key, connection, and default model.
- Example response:
  ```json
  {"status": "ok", "models_count": 8, "default_model": "gpt-3.5-turbo"}
  ```

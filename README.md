
# AI Website with Assistant (Demo Mode Fallback)

This Flask app uses OpenAI's API (v1.x). If API access fails or is not configured, it falls back to a local demo mode.

## 🚀 Deployment on Render

1. Create a **New Web Service** on [render.com](https://render.com).
2. Connect this repo.
3. Set environment variables (optional):
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
- Demo Mode response:
  ```json
  {"status": "demo", "details": "Running in Demo Mode – OpenAI API not configured or unavailable."}
  ```

## 🧪 Demo Mode

If OpenAI API is not available, all responses will be placeholder demo replies:
```
(Demo Mode) You asked: 'Your question'. This is a placeholder response.
```

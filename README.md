
# AI Website with Assistant (OpenAI v1.x, Proxies Removed)

This is a Flask app combining a static frontend with an AI backend using OpenAI's API (v1.x).

## 🚀 Deployment on Render

1. Create a **New Web Service** on [render.com](https://render.com).
2. Connect this repo.
3. Set the environment variable:
   ```
   OPENAI_API_KEY=sk-your-openai-key
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

- Visit `/health` to verify the API key and connection to OpenAI.
- Example response:
  ```json
  {"status": "ok", "models_count": 8}
  ```
- If error:
  ```json
  {"status": "error", "details": "Invalid API key"}
  ```

## ⚠️ Proxy Environment Variables

This app removes any proxy settings from the environment:
```
HTTP_PROXY, HTTPS_PROXY, http_proxy, https_proxy
```
to avoid OpenAI client errors.

Make sure you do NOT set these in Render unless required for your network.

# ⚡ Quick Deploy on Render (5 Minutes)

## 🎯 TL;DR

1. **Backend**: Render → New Web Service → Root: `backend` → Deploy
2. **Frontend**: Render → New Static Site → Root: `frontend` → Deploy
3. **Connect**: Add URLs to environment variables

---

## Step-by-Step

### 1️⃣ Backend (2 min)

```
1. render.com → New + → Web Service
2. Connect GitHub → Select repo
3. Settings:
   - Root Directory: backend
   - Build: pip install -r requirements.txt
   - Start: uvicorn main:app --host 0.0.0.0 --port $PORT
4. Environment:
   - SECRET_KEY: (generate random string)
   - ALLOWED_ORIGINS: (leave empty for now)
5. Deploy → Copy URL
```

### 2️⃣ Frontend (2 min)

```
1. render.com → New + → Static Site
2. Connect GitHub → Select same repo
3. Settings:
   - Root Directory: frontend
   - Build: npm install && npm run build
   - Publish: dist
4. Environment:
   - VITE_API_URL: [Your Backend URL]
5. Deploy → Copy URL
```

### 3️⃣ Connect (1 min)

```
1. Backend → Environment → ALLOWED_ORIGINS
   - Value: [Your Frontend URL]
2. Redeploy both services
```

---

## ✅ Done!

Visit your frontend URL and test!

**Need details?** See [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md)


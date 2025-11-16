# 🚀 How to Deploy on Render

## Quick Start

**Both frontend and backend will be deployed on Render.**

### 📋 Prerequisites

1. Code pushed to GitHub
2. Render account (sign up at [render.com](https://render.com))

---

## 🎯 Deployment Steps

### Step 1: Deploy Backend

1. Go to [render.com](https://render.com) → Sign in
2. Click **"New +"** → **"Web Service"**
3. **Connect GitHub** → Select your repository
4. **Configure:**
   - **Name**: `event-review-summarizer-backend`
   - **Root Directory**: `backend` ⚠️ **IMPORTANT**
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Environment Variables:**
   - `SECRET_KEY`: Generate a random string
   - `ALLOWED_ORIGINS`: Leave empty for now
6. Click **"Create Web Service"**
7. **Wait for deployment** (3-5 minutes)
8. **Copy the backend URL** (e.g., `https://your-backend.onrender.com`)

### Step 2: Deploy Frontend

1. In Render dashboard, click **"New +"** → **"Static Site"**
2. **Connect GitHub** → Select the same repository
3. **Configure:**
   - **Name**: `event-review-summarizer-frontend`
   - **Root Directory**: `frontend` ⚠️ **IMPORTANT**
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist`
4. **Environment Variables:**
   - `VITE_API_URL`: Your backend URL from Step 1
5. Click **"Create Static Site"**
6. **Wait for deployment** (2-3 minutes)
7. **Copy the frontend URL** (e.g., `https://your-frontend.onrender.com`)

### Step 3: Connect Frontend and Backend

1. **Backend Service** → **Environment** tab
2. Update `ALLOWED_ORIGINS`:
   - Value: Your frontend URL from Step 2
3. **Redeploy Backend**: Click "Manual Deploy" → "Deploy latest commit"
4. **Redeploy Frontend**: Click "Manual Deploy" → "Deploy latest commit"

---

## ✅ Test Your Deployment

1. Visit your frontend URL
2. Register a new account
3. Login
4. Upload a CSV file
5. View the analysis results

If everything works, you're done! 🎉

---

## 🔧 Troubleshooting

### Backend won't start
- ✅ Check Root Directory is set to `backend`
- ✅ Check build logs for errors
- ✅ Verify `requirements.txt` exists

### Frontend can't connect to backend
- ✅ Check `VITE_API_URL` is set correctly
- ✅ Check `ALLOWED_ORIGINS` includes your frontend URL
- ✅ Make sure both services are deployed

### CORS errors
- ✅ Update `ALLOWED_ORIGINS` with your frontend URL
- ✅ Redeploy backend after updating

---

## 📚 Detailed Guide

For more detailed instructions, see [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md)

For quick reference, see [QUICK_DEPLOY_RENDER.md](./QUICK_DEPLOY_RENDER.md)

---

## 🎯 Environment Variables Summary

### Backend
```
SECRET_KEY=your-random-secret-key
ALLOWED_ORIGINS=https://your-frontend.onrender.com
```

### Frontend
```
VITE_API_URL=https://your-backend.onrender.com
```

---

**That's it! Your app is now live on Render! 🚀**


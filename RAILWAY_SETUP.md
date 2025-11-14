# Railway Deployment Setup 🚂

## Quick Fix for Railway Error

Railway needs to know:
1. **Root Directory**: `backend`
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## ✅ Step-by-Step Setup

### Step 1: Configure in Railway Dashboard

1. Go to your Railway project
2. Click on your service
3. Go to **"Settings"** tab
4. Scroll to **"Service Settings"**

**Set these values:**

- **Root Directory**: `backend`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 2: Add Environment Variables

In Railway Dashboard → **Variables** tab:

- `SECRET_KEY`: Generate a random string (e.g., use Railway's "Generate" button)
- `ALLOWED_ORIGINS`: Your frontend URL (add after frontend deployment)
- `PORT`: Railway sets this automatically (don't override)

### Step 3: Deploy

1. Railway will auto-deploy when you push to GitHub
2. Or click **"Deploy"** → **"Deploy from GitHub"**

## 📁 Files Created

I've created `backend/railway.json` which Railway can auto-detect, but the manual settings above are more reliable.

## 🔍 Verify

After deployment, check the logs. You should see:
```
Installing dependencies...
Starting uvicorn...
Application startup complete.
```

## 🎯 Quick Configuration Summary

**In Railway Dashboard:**
- Root Directory: `backend` ✅
- Build Command: `pip install -r requirements.txt` ✅
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT` ✅

That's it! Railway should work now.

## 🆘 Still Having Issues?

1. **Check Root Directory**: Must be `backend` (not root)
2. **Check Build Logs**: Look for Python version and dependency installation
3. **Verify Procfile**: Should exist in `backend/` directory

---

**The key is setting the Root Directory to `backend` in Railway settings!** 🎯


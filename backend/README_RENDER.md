# Render Deployment Guide

## ⚠️ Important: Python Version

**Render defaults to Python 3.13**, but pandas 2.1.4 requires Python 3.12 or earlier.

## ✅ Solution

### Method 1: Use runtime.txt (Automatic)

The `runtime.txt` file in this directory specifies Python 3.12.0. Render will automatically detect and use it.

### Method 2: Manual Configuration

1. In Render Dashboard → Your Service → Settings
2. Under "Environment" section
3. Set **Python Version** to: `3.12.0`
4. Save and redeploy

### Method 3: Use render.yaml

The `render.yaml` file contains the configuration. Render will use it automatically if present.

## 🔧 Build Settings

- **Root Directory**: `backend` (if deploying from monorepo)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## 🌐 Environment Variables

Required:
- `SECRET_KEY`: Generate a secure random string
- `ALLOWED_ORIGINS`: Your frontend URL (e.g., `https://your-app.vercel.app`)

Optional:
- `DATABASE_URL`: For PostgreSQL (defaults to SQLite)

## 🐛 Troubleshooting

### Build Fails with Pandas Error

**Error**: `too few arguments to function '_PyLong_AsByteArray'`

**Solution**: 
1. Verify Python version is 3.12.0 (check build logs)
2. Ensure `runtime.txt` exists with `python-3.12.0`
3. Clear build cache and redeploy

### Module Not Found Errors

**Solution**: 
1. Check that `Root Directory` is set to `backend`
2. Verify `requirements.txt` is in the backend directory
3. Check build logs for missing dependencies

## 📝 Quick Checklist

- [ ] `runtime.txt` exists with `python-3.12.0`
- [ ] Root Directory set to `backend`
- [ ] Environment variables configured
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## 🚀 After Deployment

1. Copy your Render URL (e.g., `https://your-app.onrender.com`)
2. Update frontend `VITE_API_URL` environment variable
3. Update `ALLOWED_ORIGINS` in Render with your frontend URL


# 🚀 Complete Render Deployment Guide

Deploy both frontend and backend on Render in minutes!

## 📋 Overview

- **Backend**: Python FastAPI service on Render
- **Frontend**: Static site (React/Vite) on Render
- **Both services**: Deployed from the same GitHub repository

---

## Part 1: Push to GitHub

### Step 1: Commit and Push

```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

---

## Part 2: Deploy Backend on Render

> **Note**: The ML model is already integrated into the backend. No separate deployment needed! See [ML_DEPLOYMENT.md](./ML_DEPLOYMENT.md) for details.

### Step 1: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click **"New +"** → **"Web Service"**

### Step 2: Connect GitHub Repository

1. **"Connect GitHub"** → Select your repository
2. Render will detect the `backend/render.yaml` file

### Step 3: Configure Backend Service

**Service Settings:**

- **Name**: `event-review-summarizer-backend` (or any name)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main` (or your default branch)
- **Root Directory**: `backend` ⚠️ **CRITICAL**
- **Build Command**: `python copy_ml_files.py && pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**OR** - Render will auto-detect from `backend/render.yaml` if you use "Apply Render YAML"

⚠️ **Important**: 
- Root Directory must be `backend`
- The build command automatically copies `ML/src/` files into `backend/ml_src/` during deployment
- This ensures ML code is accessible even when root directory is set to `backend`

### Step 4: Add Environment Variables

**Environment** tab → Add:

- `SECRET_KEY`: Click "Generate" or use a random string (e.g., `openssl rand -hex 32`)
- `ALLOWED_ORIGINS`: Leave empty for now (add after frontend deployment)

> **ML Model Note**: The ML model will download automatically on first use (~500MB, takes 1-2 minutes). This is normal!

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will start building
3. Wait for deployment to complete (usually 3-5 minutes)
4. **Copy the URL** - Example: `https://event-review-summarizer-backend.onrender.com`

---

## Part 3: Deploy Frontend on Render

### Step 1: Create Static Site

1. In Render dashboard, click **"New +"** → **"Static Site"**
2. **"Connect GitHub"** → Select the same repository

### Step 2: Configure Frontend Service

**Static Site Settings:**

- **Name**: `event-review-summarizer-frontend` (or any name)
- **Branch**: `main` (or your default branch)
- **Root Directory**: `frontend` ⚠️ **IMPORTANT**
- **Build Command**: `npm install && npm run build`
- **Publish Directory**: `dist`

**OR** - Render will auto-detect from `frontend/render.yaml` if you use "Apply Render YAML"

### Step 3: Add Environment Variable

**Environment** tab → Add:

- **Key**: `VITE_API_URL`
- **Value**: Your backend URL (e.g., `https://event-review-summarizer-backend.onrender.com`)

⚠️ **Important**: Environment variables starting with `VITE_` are available in your React app during build time.

### Step 4: Deploy

1. Click **"Create Static Site"**
2. Render will start building
3. Wait for deployment to complete (usually 2-3 minutes)
4. **Copy the URL** - Example: `https://event-review-summarizer-frontend.onrender.com`

---

## Part 4: Connect Frontend and Backend

### Step 1: Update Backend CORS

**In Backend Service → Environment:**

1. Update `ALLOWED_ORIGINS`
2. Value: Your frontend URL (e.g., `https://event-review-summarizer-frontend.onrender.com`)
3. If you have multiple, separate with commas:
   ```
   https://event-review-summarizer-frontend.onrender.com,http://localhost:3000
   ```

### Step 2: Update Frontend API URL

**In Frontend Service → Environment:**

1. Verify `VITE_API_URL` is set to your backend URL
2. Make sure it's correct (no trailing slash)

### Step 3: Redeploy Both

1. **Backend**: Click "Manual Deploy" → "Deploy latest commit" (to pick up new CORS setting)
2. **Frontend**: Click "Manual Deploy" → "Deploy latest commit" (to rebuild with correct API URL)

---

## ✅ Verify Everything Works

1. **Visit your frontend URL**: `https://event-review-summarizer-frontend.onrender.com`
2. **Register/Login**: Should work
3. **Upload CSV**: Should connect to backend
4. **View Results**: Should display analysis

---

## 🔧 Troubleshooting

### Backend Issues

**"pip: command not found" or build fails**
- ✅ Set **Root Directory** to `backend` in Render Settings
- ✅ Verify `requirements.txt` exists in `backend/` directory

**"Module not found" errors**
- ✅ Check that all dependencies are in `backend/requirements.txt`
- ✅ Check build logs for missing packages
- ✅ Verify `ML/src/` directory exists in repository (not in `.gitignore`)
- ✅ Check build logs for `copy_ml_files.py` - should show files copied
- ✅ Verify `backend/ml_src/` directory exists after build

**CORS errors**
- ✅ Update `ALLOWED_ORIGINS` in backend environment variables
- ✅ Make sure frontend URL is correct (no trailing slash)
- ✅ Redeploy backend after updating CORS

**Python version issues**
- ✅ Render should auto-detect `backend/runtime.txt` (Python 3.12.0)
- ✅ Or manually set Python version to `3.12.0` in Render dashboard

**ML Model Issues**
- ✅ First request may take 1-2 minutes (model downloading from Hugging Face)
- ✅ Check Render logs for model download progress
- ✅ Verify enough disk space (~500MB for model)
- ✅ See [ML_DEPLOYMENT.md](./ML_DEPLOYMENT.md) for detailed ML troubleshooting

### Frontend Issues

**"API connection failed"**
- ✅ Check `VITE_API_URL` is set correctly in frontend environment variables
- ✅ Verify backend URL is accessible (visit in browser)
- ✅ Check browser console for errors
- ✅ Make sure `VITE_API_URL` starts with `https://` (not `http://`)

**"Build failed"**
- ✅ Check Node.js version (Render uses Node 18+ by default)
- ✅ Verify all dependencies in `frontend/package.json`
- ✅ Check build logs in Render dashboard

**"Page not found" or routing issues**
- ✅ Add `_redirects` file in `frontend/public/` (see below)

---

## 📝 Additional Configuration

### Frontend Routing (SPA)

Create `frontend/public/_redirects` file:

```
/*    /index.html   200
```

This ensures React Router works correctly on Render.

---

## 🎯 Quick Reference

### Backend (Render Web Service)
- **Root Directory**: `backend`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Environment Variables**: `SECRET_KEY`, `ALLOWED_ORIGINS`

### Frontend (Render Static Site)
- **Root Directory**: `frontend`
- **Build Command**: `npm install && npm run build`
- **Publish Directory**: `dist`
- **Environment Variable**: `VITE_API_URL`

---

## 📋 Deployment Checklist

### Backend
- [ ] Render account created
- [ ] Web Service created
- [ ] Root Directory set to `backend`
- [ ] Environment variables added (`SECRET_KEY`, `ALLOWED_ORIGINS`)
- [ ] Deployed successfully
- [ ] Backend URL copied

### Frontend
- [ ] Static Site created
- [ ] Root Directory set to `frontend`
- [ ] Environment variable added (`VITE_API_URL`)
- [ ] `_redirects` file created (if needed)
- [ ] Deployed successfully
- [ ] Frontend URL copied

### Connection
- [ ] `ALLOWED_ORIGINS` updated with frontend URL
- [ ] `VITE_API_URL` updated with backend URL
- [ ] Both services redeployed
- [ ] Tested end-to-end

---

## 🎉 You're Live!

Your application is now deployed on Render!

- **Frontend**: `https://event-review-summarizer-frontend.onrender.com`
- **Backend API**: `https://event-review-summarizer-backend.onrender.com`
- **API Docs**: `https://event-review-summarizer-backend.onrender.com/docs`

---

## 💡 Tips

1. **Free Tier**: Render free tier spins down after 15 minutes of inactivity. First request may take 30-60 seconds to wake up.

2. **Custom Domains**: You can add custom domains in Render dashboard → Settings → Custom Domains

3. **Auto-Deploy**: Render auto-deploys on every push to your main branch (enabled by default)

4. **Environment Variables**: Changes to environment variables require a redeploy

5. **Logs**: Check build and runtime logs in Render dashboard for debugging

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Vite Documentation](https://vitejs.dev)

---

**Need help?** Check the build logs in Render dashboard for detailed error messages.


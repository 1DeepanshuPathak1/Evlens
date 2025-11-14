# Render Deployment Fix 🔧

## Problem
Pandas 2.1.3 is incompatible with Python 3.13 (which Render uses by default).

## Solution

### Option 1: Specify Python 3.12 (Recommended)

1. **Create `runtime.txt`** in the `backend/` directory:
   ```
   python-3.12.0
   ```

2. **In Render Dashboard:**
   - Go to your service settings
   - Under "Environment", set **Python Version** to `3.12.0`
   - Or Render will automatically detect `runtime.txt`

3. **Redeploy**

### Option 2: Update Pandas Version

Update `backend/requirements.txt`:
```txt
pandas>=2.1.4  # or pandas>=2.2.0 for Python 3.13 support
```

### Option 3: Use render.yaml (Easiest)

I've created `backend/render.yaml` that specifies Python 3.12.

**In Render Dashboard:**
1. Go to your service
2. Settings → "Build & Deploy"
3. Set **Root Directory** to: `backend`
4. Render will automatically use `render.yaml` if present

## Updated Files

✅ `backend/runtime.txt` - Specifies Python 3.12
✅ `backend/render.yaml` - Render configuration
✅ `backend/requirements.txt` - Updated pandas version

## Quick Fix Steps

1. **Push the updated files to GitHub:**
   ```bash
   git add backend/runtime.txt backend/render.yaml backend/requirements.txt
   git commit -m "Fix: Add Python 3.12 runtime for Render deployment"
   git push
   ```

2. **In Render Dashboard:**
   - Go to your service
   - Click "Manual Deploy" → "Deploy latest commit"
   - Or Render will auto-deploy on push

3. **Verify Python Version:**
   - Check build logs
   - Should see: "Python 3.12.0"

## Alternative: Use Railway Instead

Railway is often easier for Python deployments:
- Automatically detects Python version
- Better error messages
- Free tier available

See [DEPLOYMENT.md](./DEPLOYMENT.md) for Railway setup.


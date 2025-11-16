# 🔧 Fix 404 Routing Issue

## Problem

Getting 404 error when accessing `/register` or other routes directly:
- `https://event-review-summarizer-frontend.onrender.com/register` → 404
- This is because Render doesn't know about React Router routes

## Solution

Render static sites need to be configured to redirect all routes to `index.html` so React Router can handle routing.

## ✅ Fix Steps

### Option 1: Configure in Render Dashboard (Recommended)

1. **Go to Render Dashboard** → Your Frontend Service
2. **Settings** tab
3. Look for **"Redirects/Rewrites"** or **"Routes"** section
4. Add a rewrite rule:
   - **Source**: `/*`
   - **Destination**: `/index.html`
   - **Type**: Rewrite (not redirect)

### Option 2: Use _redirects File (If Option 1 doesn't work)

The `_redirects` file should be copied to `dist/` during build. Verify it's there:

1. Check if `dist/_redirects` exists after build
2. If not, we need to ensure Vite copies it

### Option 3: Create Custom 404.html

If Render supports it, create a `404.html` that redirects to index.html.

## 🔍 Verify Current Setup

The `_redirects` file exists in `frontend/public/_redirects`:
```
/*    /index.html   200
```

Vite should copy this to `dist/_redirects` during build. Check Render build logs to confirm.

## 📋 Quick Fix

**In Render Dashboard:**

1. Go to your **Frontend Static Site**
2. **Settings** → Look for routing/redirects
3. Add: All routes (`/*`) → Rewrite to `/index.html`

If you can't find this option, Render might not support it for static sites. In that case:

## Alternative: Use HashRouter

If Render doesn't support rewrites, we can switch to HashRouter (URLs will have `#`):

- Current: `https://your-site.com/register`
- HashRouter: `https://your-site.com/#/register`

This always works but URLs look different.

---

**Try Option 1 first - configure in Render Dashboard!** 🚀


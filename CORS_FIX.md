# 🔧 CORS Error Fix

## Problem

You're getting this error:
```
Access to XMLHttpRequest at 'https://event-review-summarizer-backend.onrender.com/api/auth/register' 
from origin 'https://event-review-summarizer-frontend.onrender.com' 
has been blocked by CORS policy: Response to preflight request doesn't pass access control check: 
No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

## Root Cause

The CORS middleware might not be properly handling OPTIONS (preflight) requests, or the `ALLOWED_ORIGINS` environment variable isn't being read correctly.

## ✅ Fix Applied

I've updated the backend code to:
1. **Better CORS configuration** - Explicitly allows OPTIONS method
2. **Added OPTIONS handler** - Handles preflight requests
3. **Added logging** - Shows CORS configuration in logs

## 🔍 Verify Environment Variable

**In Render Dashboard → Backend Service → Environment:**

Make sure `ALLOWED_ORIGINS` is set to:
```
https://event-review-summarizer-frontend.onrender.com
```

**Important:**
- ✅ No trailing slash
- ✅ No quotes around the URL
- ✅ Exact match with your frontend URL

## 📋 Steps to Fix

### Step 1: Verify Environment Variable

1. Go to Render Dashboard
2. Select your **Backend Service**
3. Go to **Environment** tab
4. Check `ALLOWED_ORIGINS`:
   - Should be: `https://event-review-summarizer-frontend.onrender.com`
   - Should NOT have trailing slash
   - Should NOT have quotes

### Step 2: Commit and Push Code Changes

```bash
git add .
git commit -m "Fix CORS configuration for preflight requests"
git push origin main
```

### Step 3: Redeploy Backend

1. Render Dashboard → Backend Service
2. Click **"Manual Deploy"** → **"Deploy latest commit"**
3. Wait for deployment to complete

### Step 4: Check Backend Logs

After deployment, check the logs. You should see:
```
CORS Allowed Origins: ['https://event-review-summarizer-frontend.onrender.com']
```

If you see this, the environment variable is being read correctly.

### Step 5: Test Registration

1. Go to your frontend URL
2. Try to register
3. Check browser console (F12) - should not see CORS errors

## 🧪 Test CORS Directly

You can test if CORS is working by running this in browser console on your frontend:

```javascript
fetch('https://event-review-summarizer-backend.onrender.com/api/auth/register', {
  method: 'OPTIONS',
  headers: {
    'Origin': 'https://event-review-summarizer-frontend.onrender.com',
    'Access-Control-Request-Method': 'POST',
    'Access-Control-Request-Headers': 'content-type'
  }
}).then(r => {
  console.log('CORS Headers:', {
    'Access-Control-Allow-Origin': r.headers.get('Access-Control-Allow-Origin'),
    'Access-Control-Allow-Methods': r.headers.get('Access-Control-Allow-Methods'),
    'Access-Control-Allow-Headers': r.headers.get('Access-Control-Allow-Headers')
  })
}).catch(console.error)
```

## 🔍 Debugging

### Check Backend Logs

In Render Dashboard → Backend Service → Logs, look for:
- `CORS Allowed Origins: [...]` - Should show your frontend URL
- Any CORS-related errors
- OPTIONS request handling

### Check Network Tab

In browser DevTools → Network tab:
1. Try to register
2. Look for the OPTIONS request (preflight)
3. Check response headers:
   - Should have `Access-Control-Allow-Origin`
   - Should have `Access-Control-Allow-Methods`
   - Should have `Access-Control-Allow-Headers`

### Common Issues

1. **Environment variable not set**: Check Render dashboard
2. **Trailing slash**: Remove `/` from end of URL
3. **Quotes in env var**: Don't add quotes in Render
4. **Backend not redeployed**: Must redeploy after code changes

## ✅ Expected Result

After fixing:
- ✅ No CORS errors in browser console
- ✅ Registration works
- ✅ OPTIONS requests return 200 OK
- ✅ Response headers include CORS headers

---

**After committing, pushing, and redeploying, CORS should work!** 🚀


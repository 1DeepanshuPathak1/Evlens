# 🔧 Troubleshooting Deployment Issues

## Common Issues and Fixes

### Issue 1: Registration Failed - CORS or URL Issues

**Symptoms:**
- Registration fails with "Registration failed" error
- No specific error message shown

**Common Causes:**

1. **Trailing Slashes in URLs** ⚠️ **MOST COMMON**
   - ❌ Wrong: `https://backend.onrender.com/`
   - ✅ Correct: `https://backend.onrender.com` (no trailing slash)

2. **CORS Configuration**
   - `ALLOWED_ORIGINS` must match frontend URL exactly (no trailing slash)
   - Backend must be redeployed after changing CORS

3. **Environment Variables Not Set**
   - `VITE_API_URL` must be set in frontend before build
   - Frontend must be rebuilt after changing environment variables

**Fix Steps:**

1. **Remove trailing slashes:**
   - Backend `ALLOWED_ORIGINS`: `https://event-review-summarizer-frontend.onrender.com` (no `/`)
   - Frontend `VITE_API_URL`: `https://event-review-summarizer-backend.onrender.com` (no `/`)

2. **Redeploy both services:**
   - Backend: Manual Deploy → Deploy latest commit
   - Frontend: Manual Deploy → Deploy latest commit (to rebuild with new env var)

3. **Check browser console:**
   - Open browser DevTools (F12)
   - Go to Console tab
   - Look for CORS errors or network errors
   - Check Network tab to see actual API calls

4. **Check backend logs:**
   - In Render dashboard → Backend service → Logs
   - Look for error messages when registration is attempted

---

### Issue 2: Environment Variables Not Working

**Symptoms:**
- Frontend still uses `localhost:8000`
- API calls go to wrong URL

**Fix:**
1. Verify `VITE_API_URL` is set in Render frontend environment variables
2. **Important**: Frontend must be rebuilt after changing `VITE_*` variables
3. Check build logs to confirm environment variable is used
4. Clear browser cache and hard refresh (Ctrl+Shift+R)

---

### Issue 3: CORS Errors

**Symptoms:**
- Browser console shows: "Access to XMLHttpRequest blocked by CORS policy"
- Network requests fail with CORS errors

**Fix:**
1. Check `ALLOWED_ORIGINS` in backend includes frontend URL exactly
2. Remove trailing slashes from URLs
3. Redeploy backend after changing CORS
4. Check backend logs for CORS-related errors

---

### Issue 4: Backend Not Responding

**Symptoms:**
- "Network Error" or "Connection Refused"
- Backend URL returns 404 or timeout

**Fix:**
1. Verify backend URL is correct and accessible
2. Visit backend URL in browser: `https://your-backend.onrender.com`
3. Should see: `{"message": "Event Review Summarizer API", "status": "running"}`
4. Check backend logs in Render dashboard
5. Verify backend service is running (not sleeping)

---

## Quick Debugging Checklist

- [ ] Backend URL accessible in browser
- [ ] Frontend URL accessible in browser
- [ ] No trailing slashes in environment variables
- [ ] `ALLOWED_ORIGINS` matches frontend URL exactly
- [ ] `VITE_API_URL` matches backend URL exactly
- [ ] Both services redeployed after env var changes
- [ ] Browser console checked for errors
- [ ] Backend logs checked for errors
- [ ] Browser cache cleared

---

## Testing the Connection

1. **Test Backend:**
   ```
   Visit: https://your-backend.onrender.com
   Should see: {"message": "Event Review Summarizer API", "status": "running"}
   ```

2. **Test API Endpoint:**
   ```
   Visit: https://your-backend.onrender.com/docs
   Should see: FastAPI documentation
   ```

3. **Test from Browser Console:**
   ```javascript
   // In browser console on frontend page
   fetch('https://your-backend.onrender.com/api/auth/register', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({
       email: 'test@test.com',
       username: 'testuser',
       password: 'test123'
     })
   }).then(r => r.json()).then(console.log).catch(console.error)
   ```

---

## Still Not Working?

1. **Check Render Logs:**
   - Backend → Logs tab
   - Frontend → Logs tab
   - Look for error messages

2. **Check Browser Console:**
   - Open DevTools (F12)
   - Console tab: Look for errors
   - Network tab: Check API requests and responses

3. **Verify Environment Variables:**
   - Backend: Settings → Environment
   - Frontend: Settings → Environment
   - Make sure values are correct (no quotes, no trailing slashes)

4. **Test Backend Directly:**
   - Use Postman or curl to test backend endpoints
   - This helps isolate if issue is frontend or backend


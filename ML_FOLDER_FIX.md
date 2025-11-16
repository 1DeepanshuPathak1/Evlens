# 🔧 ML Folder Deployment Fix

## Problem

When deploying on Render with **Root Directory** set to `backend`, the `ML/` folder (which is outside `backend/`) may not be accessible, causing import errors.

## Solution

A build script (`backend/copy_ml_files.py`) automatically copies `ML/src/` files into `backend/ml_src/` during deployment.

### How It Works

1. **During Build**: `copy_ml_files.py` runs and copies all `.py` files from `ML/src/` to `backend/ml_src/`
2. **At Runtime**: `ml_service.py` looks for ML code in multiple locations:
   - First: `backend/ml_src/` (copied during build) ✅
   - Second: `../ML/src/` (if accessible)
   - Third: `ML/src/` (from root)

### Files Created

- `backend/copy_ml_files.py` - Script to copy ML files
- `backend/ml_src/` - Generated directory (ignored by git)
- Updated `backend/ml_service.py` - Now checks multiple paths
- Updated `backend/render.yaml` - Build command includes copy step

### Build Command

```bash
python copy_ml_files.py && pip install -r requirements.txt
```

This ensures:
1. ML files are copied to `backend/ml_src/`
2. Dependencies are installed
3. Everything is ready for deployment

---

## ✅ Verification

After deployment, check Render logs for:
```
Copied 3 files from ML/src to backend/ml_src:
  - analyzer.py
  - inference.py
  - summarizer.py
```

If you see this, the ML files were successfully copied!

---

## 🎯 Summary

- ✅ ML folder is outside backend, but that's OK!
- ✅ Build script copies ML files during deployment
- ✅ Backend can access ML code from `backend/ml_src/`
- ✅ Works perfectly on Render with Root Directory = `backend`

**No separate ML deployment needed!** 🚀


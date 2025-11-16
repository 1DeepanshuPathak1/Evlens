# 🤖 ML Model Deployment Guide

## ✅ Good News: ML Model is Already Integrated!

**You do NOT need to deploy the ML model separately.** It's already part of your backend!

---

## 📋 How It Works

### Current Architecture

```
Backend (Render)
├── FastAPI Application
├── ML Service (ml_service.py)
│   ├── Loads Hugging Face model: google/flan-t5-base
│   ├── Uses ML/src/analyzer.py for CSV analysis
│   └── Generates summaries and sentiment analysis
└── All dependencies in requirements.txt
```

### Model Loading

1. **Lazy Loading**: The ML model is loaded only when needed (first CSV upload)
2. **Model Source**: Downloads from Hugging Face automatically (`google/flan-t5-base`)
3. **Location**: Model is cached in Render's filesystem after first download
4. **Memory**: Model uses ~500MB RAM when loaded

---

## 🚀 Deployment Considerations

### What Gets Deployed

When you deploy the backend on Render:
- ✅ `backend/` directory (all backend code)
- ✅ `ML/src/` directory (copied to `backend/ml_src/` during build)
- ✅ All dependencies from `requirements.txt`
- ✅ Model downloads automatically on first use

**Important**: The build process automatically copies `ML/src/` files into `backend/ml_src/` so they're accessible when root directory is set to `backend`.

### What's NOT Needed

- ❌ Separate ML service deployment
- ❌ Pre-downloading models
- ❌ ML-specific environment variables
- ❌ Separate ML server

---

## ⚙️ Render Configuration

### Backend Service Settings

Your backend on Render should have:

**Root Directory**: `backend` ⚠️ **CRITICAL**

This ensures:
- Backend code is accessible
- `ML/src/` is accessible (via relative path from backend)
- All dependencies install correctly

### Build Process

1. **Install Dependencies**: `pip install -r requirements.txt`
   - This installs: transformers, torch, pandas, scikit-learn, etc.
   - Model files are NOT included (downloaded on first use)

2. **First Request**: 
   - Model downloads from Hugging Face (~500MB)
   - Takes 1-2 minutes on first use
   - Cached for subsequent requests

---

## 📊 Model Details

### Model Information

- **Model**: `google/flan-t5-base`
- **Type**: Text summarization
- **Size**: ~500MB
- **Device**: CPU (configured in `ml_service.py`)
- **Download**: Automatic from Hugging Face

### Performance

- **First Load**: 30-60 seconds (download + load)
- **Subsequent Loads**: 5-10 seconds (from cache)
- **Memory Usage**: ~500MB RAM
- **Inference Speed**: ~1-2 seconds per summary

---

## 🔧 Troubleshooting

### Model Download Issues

**Problem**: Model fails to download on Render

**Solutions**:
1. Check internet connectivity in Render logs
2. Verify Hugging Face is accessible
3. Check disk space (model needs ~500MB)

### Memory Issues

**Problem**: Out of memory errors

**Solutions**:
1. Render free tier has 512MB RAM (may be tight)
2. Consider upgrading to paid tier (2GB+ RAM)
3. Or use a smaller model (update `ml_service.py`)

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'analyzer'`

**Solutions**:
1. Verify `ML/src/analyzer.py` exists
2. Check Root Directory is set to `backend`
3. Verify `ML/src/` is not in `.gitignore`

---

## 💡 Optimization Tips

### 1. Model Caching

The model is cached after first download. Render's filesystem persists between deployments, so the model won't re-download unless you clear the cache.

### 2. Memory Management

- Model is loaded lazily (only when needed)
- Consider using a smaller model for production if memory is tight
- Monitor memory usage in Render dashboard

### 3. Performance

- First request after deployment will be slow (model download)
- Subsequent requests are faster (model cached)
- Consider warming up the model on deployment

---

## 🔄 Updating the Model

### To Use a Different Model

1. Edit `backend/ml_service.py`:
   ```python
   _summarizer = pipeline(
       "summarization",
       model="your-model-name",  # Change this
       device=-1
   )
   ```

2. Redeploy backend
3. Model will download automatically

### Popular Alternatives

- `facebook/bart-large-cnn` (better quality, larger)
- `google/pegasus-xsum` (specialized for summarization)
- `t5-small` (smaller, faster)

---

## ✅ Deployment Checklist

- [ ] Backend Root Directory set to `backend`
- [ ] `ML/src/` directory is in repository (not ignored)
- [ ] All ML dependencies in `backend/requirements.txt`
- [ ] First request tested (model download)
- [ ] Memory usage monitored
- [ ] Model caching verified

---

## 📚 Additional Resources

- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Render Memory Limits](https://render.com/docs/instance-types)
- [Model Optimization Guide](https://huggingface.co/docs/transformers/perf_infer_cpu)

---

## 🎯 Summary

**TL;DR**: 
- ✅ ML model is part of backend
- ✅ No separate deployment needed
- ✅ Model downloads automatically
- ✅ Just deploy backend normally!

**The ML model will work automatically when you deploy your backend on Render!** 🚀


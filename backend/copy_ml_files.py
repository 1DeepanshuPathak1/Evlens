"""
Script to copy ML/src files into backend for deployment
This ensures ML code is available when root directory is set to 'backend'
"""
import os
import shutil
import sys

def copy_ml_files():
    """Copy ML/src files to backend/ml_src/"""
    # Get current directory (backend/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Get project root (one level up)
    root_dir = os.path.dirname(current_dir)
    # Source: ML/src
    ml_src_dir = os.path.join(root_dir, "ML", "src")
    # Destination: backend/ml_src
    dest_dir = os.path.join(current_dir, "ml_src")
    
    # Check if ML/src exists
    if not os.path.exists(ml_src_dir):
        print(f"Warning: ML/src directory not found at {ml_src_dir}")
        print("This is normal if ML/src is already in backend/")
        return
    
    # Create destination directory
    os.makedirs(dest_dir, exist_ok=True)
    
    # Copy all Python files from ML/src
    files_copied = []
    for file in os.listdir(ml_src_dir):
        if file.endswith('.py'):
            src_file = os.path.join(ml_src_dir, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)
            files_copied.append(file)
    
    if files_copied:
        print(f"Copied {len(files_copied)} files from ML/src to backend/ml_src:")
        for f in files_copied:
            print(f"  - {f}")
    else:
        print("No Python files found in ML/src")

if __name__ == "__main__":
    copy_ml_files()


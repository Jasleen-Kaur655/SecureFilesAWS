import os
import json
import hashlib
from datetime import datetime, timedelta

DATABASE_FILE = "database.json"
STORAGE_DIR = "storage"

# Ensure storage exists
os.makedirs(STORAGE_DIR, exist_ok=True)

def save_file(file):
    file_path = os.path.join(STORAGE_DIR, file.filename)
    
    # Versioning
    version = 1
    base, ext = os.path.splitext(file.filename)
    while os.path.exists(file_path):
        version += 1
        file_path = os.path.join(STORAGE_DIR, f"{base}_v{version}{ext}")
    
    # Save file
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    # Calculate hash
    file_hash = hashlib.sha256(open(file_path, "rb").read()).hexdigest()
    
    # Store metadata
    data = load_db()
    data["files"].append({
        "filename": os.path.basename(file_path),
        "hash": file_hash,
        "upload_time": datetime.utcnow().isoformat(),
        "status": "UPLOADED",
        "expiry": (datetime.utcnow() + timedelta(days=7)).isoformat()
    })
    save_db(data)
    
    return file_path

def get_file_list():
    data = load_db()
    return data["files"]

def download_file(filename):
    path = os.path.join(STORAGE_DIR, filename)
    return path if os.path.exists(path) else None

def load_db():
    if not os.path.exists(DATABASE_FILE):
        return {"files": []}
    with open(DATABASE_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=2)

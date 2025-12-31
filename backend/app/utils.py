from datetime import datetime
from file_service import load_db, save_db, STORAGE_DIR
import os

# Delete expired files
def cleanup_expired_files():
    data = load_db()
    now = datetime.utcnow()
    new_files = []
    for f in data["files"]:
        expiry = datetime.fromisoformat(f["expiry"])
        if expiry < now:
            path = os.path.join(STORAGE_DIR, f["filename"])
            if os.path.exists(path):
                os.remove(path)
        else:
            new_files.append(f)
    data["files"] = new_files
    save_db(data)

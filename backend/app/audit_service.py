from datetime import datetime

AUDIT_FILE = "audit.log"

def log_event(user_id, action, file_name, sensitive_fields):
    with open(AUDIT_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} | {user_id} | {action} | {file_name} | {sensitive_fields}\n")

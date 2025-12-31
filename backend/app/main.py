from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from auth_service import authenticate, verify_token
from file_service import save_file, get_file_list, download_file
from ai_guard import check_sensitive
from audit_service import log_event

app = FastAPI()

# Health check
@app.get("/")
def home():
    return {"status": "Backend running"}

# Login
@app.post("/login")
def login(username: str, password: str):
    token = authenticate(username, password)
    if token:
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Upload file
@app.post("/upload")
def upload_file(file: UploadFile = File(...), token: str = Depends(verify_token)):
    # Save file locally
    file_path = save_file(file)
    
    # Check sensitive data
    sensitive_fields = check_sensitive(file_path)
    
    # Move to quarantine if sensitive
    if sensitive_fields:
        from shutil import move
        move(file_path, f"quarantine/{file.filename}")
        status = "SENSITIVE"
    else:
        status = "SAFE"
    
    # Log audit
    log_event(token["user_id"], "UPLOAD", file.filename, sensitive_fields)
    
    return {"filename": file.filename, "status": status, "sensitive_fields": sensitive_fields}

# List files
@app.get("/files")
def list_files(token: str = Depends(verify_token)):
    files = get_file_list()
    return {"files": files}

# Download file
@app.get("/download/{filename}")
def download(filename: str, token: str = Depends(verify_token)):
    file_path = download_file(filename)
    if not file_path:
        raise HTTPException(status_code=404, detail="File not found")
    log_event(token["user_id"], "DOWNLOAD", filename, [])
    return {"file_path": file_path}  # In real UI, send StreamingResponse

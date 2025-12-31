from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "MY_SECRET_KEY"

# Hardcoded users for demo
USERS = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

def authenticate(username: str, password: str):
    user = USERS.get(username)
    if user and user["password"] == password:
        payload = {
            "user_id": username,
            "role": user["role"],
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token
    return None

def verify_token(token: str):
    from fastapi import HTTPException
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

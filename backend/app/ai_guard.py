import re

# Example patterns: Credit Card, My Number, Name
PATTERNS = {
    "credit_card": r"\b\d{16}\b",
    "my_number": r"\b\d{12}\b",
    "name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
}

def check_sensitive(file_path):
    sensitive_found = []
    try:
        with open(file_path, "r", errors="ignore") as f:
            text = f.read()
        for key, pattern in PATTERNS.items():
            if re.search(pattern, text):
                sensitive_found.append(key)
    except Exception:
        pass
    return sensitive_found


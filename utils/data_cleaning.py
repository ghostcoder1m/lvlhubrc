def clean_email(email: str) -> str:
    """Standardize email format."""
    return email.strip().lower()

def clean_phone(phone: str) -> str:
    """Standardize phone number format."""
    return phone.strip().replace(" ", "").replace("-", "")

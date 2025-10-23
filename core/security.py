'''
import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from hashlib import sha256
from core.config import settings  # ✅ import your Settings class
import logging

# =====================================================
# LOGGING SETUP (Optional for debugging)
# =====================================================
logger = logging.getLogger(__name__)

# =====================================================
# PASSWORD HASHING CONFIG
# =====================================================
# ✅ Option 1 — Use bcrypt (recommended, compatible)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ✅ Option 2 — Use Argon2 (more secure, optional)
# To use Argon2, install with: pip install passlib[argon2]
# pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# =====================================================
# PASSWORD UTILITIES
# =====================================================

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt, safely handling long passwords.
    If password exceeds 72 bytes (bcrypt limit), pre-hash with SHA256 first.
    """
    if len(password.encode()) > 72:
        password = sha256(password.encode()).hexdigest()
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against the stored hash.
    Handles SHA256 pre-hashing for long passwords automatically.
    """
    if len(plain_password.encode()) > 72:
        plain_password = sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(plain_password, hashed_password)

# =====================================================
# JWT TOKEN UTILITIES
# =====================================================

def create_access_token(data: dict) -> str:
    """
    Generate a JWT access token with expiration.
    """
    to_encode = data.copy()
    expire_minutes = getattr(settings, "ACCESS_TOKEN_EXPIRE_MINUTES", 60)
    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token


def verify_access_token(token: str):
    """
    Verify JWT validity and decode payload.
    Returns decoded payload if valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError as e:
        logger.warning(f"Invalid or expired JWT: {e}")
        return None
'''
import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from core.config import settings  # ✅ make sure you have your Settings class here
import logging

# =====================================================
# LOGGING SETUP (Optional for debugging)
# =====================================================
logger = logging.getLogger(__name__)

# =====================================================
# PASSWORD HASHING CONFIG
# =====================================================
# Use bcrypt_sha256 to automatically handle passwords > 72 bytes
pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

# =====================================================
# PASSWORD UTILITIES
# =====================================================

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt_sha256.
    Handles long passwords safely without manual SHA256 pre-hash.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against the stored hash.
    Works with bcrypt_sha256.
    """
    return pwd_context.verify(plain_password, hashed_password)

# =====================================================
# JWT TOKEN UTILITIES
# =====================================================

def create_access_token(data: dict) -> str:
    """
    Generate a JWT access token with expiration.
    """
    to_encode = data.copy()
    expire_minutes = getattr(settings, "ACCESS_TOKEN_EXPIRE_MINUTES", 60)
    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def verify_access_token(token: str):
    """
    Verify JWT validity and decode payload.
    Returns decoded payload if valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except JWTError as e:
        logger.warning(f"Invalid or expired JWT: {e}")
        return None

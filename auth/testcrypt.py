from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "your_very_long_password_here"

# SHA256 pre-hash as hex string
sha256_hash_hex = hashlib.sha256(password.encode('utf-8')).hexdigest()  # 64 chars < 72 bytes

# Hash with bcrypt
hashed = pwd_context.hash(sha256_hash_hex)
print("Hashed:", hashed)
b="uzair"
# Verify
verify_result = pwd_context.verify(hashlib.sha256(password.encode('utf-8')).hexdigest(), hashed)
print("Verified:", verify_result)
print(len(b.encode('utf-8')))

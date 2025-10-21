
from core.security import hash_password, verify_password

pwd = "a" * 100
hashed = hash_password(pwd)
print("Hash:", hashed)
print("Verified:", verify_password(pwd, hashed))  # ✅ Should print True

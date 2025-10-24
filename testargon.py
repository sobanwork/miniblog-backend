from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

h = pwd_context.hash("testpassword")
print("Hash:", h)
print("Verify:", pwd_context.verify("testpassword", h))

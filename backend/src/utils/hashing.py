from passlib.context import CryptContext
import hashlib
import bcrypt

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
   
    sha_hash = hashlib.sha256(password.encode()).digest()
    return bcrypt.hashpw(sha_hash, bcrypt.gensalt())

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# a="rohit"
# print(hash_password(a))
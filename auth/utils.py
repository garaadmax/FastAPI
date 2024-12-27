import jwt
import logging
import uuid
from datetime import datetime, timedelta, timezone
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from passlib.context import CryptContext
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

passwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=12)
ACCESS_TOKEN_EXPIRY = Config.ACCESS_TOKEN_EXPIRY


def generate_passwd_hash(password: str) -> str:
    return passwd_context.hash(password)


def verify_password(password: str, hashes: str) -> bool:
    return passwd_context.verify(password, hashes)


def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    if not isinstance(user_data, dict):
        raise ValueError("user_data must be a dictionary.")
    payload = {
        "user": user_data,
        "exp": datetime.now(timezone.utc) + (expiry or timedelta(seconds=ACCESS_TOKEN_EXPIRY)),
        "jti": str(uuid.uuid4()),
        "refresh": refresh,
    }
    try:
        return jwt.encode(payload=payload, key=Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)
    except jwt.PyJWTError as e:
        raise RuntimeError(f"Error creating access token: {e}")


def decode_token(token: str):
    if not isinstance(token, str) or not token:
        logging.error("Invalid token format")
        return None
    try:
        return jwt.decode(jwt=token, key=Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM])
    except jwt.PyJWTError as e:
        logging.error(f"Token decoding error: {e}")
        return None


serializer = URLSafeTimedSerializer(secret_key=Config.JWT_SECRET, salt=Config.MAIL_SALT)


def create_url_safe_token(data: dict):
    return serializer.dumps(data)


def decode_url_safe_token(token: str):
    try:
        return serializer.loads(token)
    except (BadSignature, SignatureExpired) as e:
        logging.error(f"Token decoding error: {e}")
        return None

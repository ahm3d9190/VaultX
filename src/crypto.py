import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password: str, salt: bytes) -> bytes:
    """Generates a key from a password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_message(message: str, password: str) -> str:
    """Encrypts a message with a password."""
    salt = b'salt_'  # In a real app, use a unique salt for each user
    key = generate_key(password, salt)
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message: str, password: str) -> str:
    """Decrypts a message with a password."""
    salt = b'salt_'  # In a real app, use the same salt used for encryption
    key = generate_key(password, salt)
    f = Fernet(key)
    try:
        decrypted_message = f.decrypt(encrypted_message.encode())
        return decrypted_message.decode()
    except Exception as e:
        # In a real app, handle different exceptions (e.g., InvalidToken)
        return "Decryption failed. Invalid password or corrupted message."

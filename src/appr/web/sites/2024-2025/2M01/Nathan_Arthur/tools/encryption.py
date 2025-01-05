import hashlib
from cryptography.fernet import Fernet
import base64

def resolveUserPwdToKey(user, pwd) -> str:
    combined = user + pwd
    hashed_key = hashlib.sha256(combined.encode('utf-8')).digest()
    assert len(hashed_key) == 32
    encoded_key = base64.urlsafe_b64encode(hashed_key).decode('utf-8')
    return encoded_key

def readAndDecrypteFile(key, filePath):
    decrypted_lines = []
    with open(filePath, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                decrypted_line = decrypt_str(key, line)
                decrypted_lines.append(decrypted_line)
    return decrypted_lines

def encrypteAndWriteFile(key, lines, filePath):
    encrypted_lines = []
    for line in lines:
        encrypted_line = encrypt_str(key, line)
        encrypted_lines.append(encrypted_line)
    with open(filePath, "w", encoding="utf-8") as file:
        for line in encrypted_lines:
            file.write(line + "\n")

def encrypt_str(key: str, str: str) -> str:
    fernet = Fernet(key)
    usr_bytes = str.encode('utf-8')
    encrypted_data = fernet.encrypt(usr_bytes)
    return encrypted_data.decode('utf-8')

def decrypt_str(key: str, str: str) -> str:
    fernet = Fernet(key)
    encrypted_bytes = str.encode('utf-8')
    decrypted_data = fernet.decrypt(encrypted_bytes)
    return decrypted_data.decode('utf-8')
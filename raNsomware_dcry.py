import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import platform  # Importing platform module

# predefined password
PASSWORD = "Your Password" # Replace this with a strong password

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data[32:]) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def decrypt_file(file_path: str, password: str) -> None:
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    data = decrypt_data(encrypted_data, password)
    original_file_path = file_path.replace(".enc", "")
    with open(original_file_path, "wb") as f:
        f.write(data)
    os.remove(file_path)
    print(f"Decrypted and deleted {file_path} -> {original_file_path}")

def decrypt_folder(folder_path: str, password: str) -> None:
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".enc"):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, password)

def main():
    ascii_art = """
 _   _ _   _    
| \ | (_) | |   
|  \| |_  | | __
| . ` | | | |/ /
| |\  | | |   < 
|_| \_|_| |_|\_\ 
"""
    print(ascii_art)

    # Detect operating system
    os_type = platform.system()
    if os_type == "Windows":
            target = r"C:\\Users\\%USERNAME%\\Desktop\\Nik"
    elif os_type == "Linux":
        target = "/root"
    else:
        print("Unsupported OS.")
        return

    # Automatically decrypt based on detected OS
    if os.path.isdir(target):
        decrypt_folder(target, PASSWORD)
        print(f"Decrypted all files in {target}")
    else:
        print(f"Invalid target directory: {target}")

if __name__ == "__main__":
    main()

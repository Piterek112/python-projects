from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Generowanie losowego klucza i wektora inicjalizacji
key = os.urandom(32)
iv = os.urandom(16)

# Inicjalizacja algorytmu AES w trybie CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Szyfrowanie
encryptor = cipher.encryptor()
padder = padding.PKCS7(128).padder()
plaintext = input("Wpisz tekst do zaszyfrowania: ").encode()
padded_plaintext = padder.update(plaintext) + padder.finalize()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

# Deszyfrowanie
decryptor = cipher.decryptor()
unpadder = padding.PKCS7(128).unpadder()
decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()

print('Zaszyfrowany tekst:', ciphertext)
print('Odszyfrowany tekst:', unpadded_decrypted_text.decode())

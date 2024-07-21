import tkinter as tk
from tkinter import ttk, messagebox
import string
import math
from pyDes import des, PAD_PKCS5
from Crypto.Cipher import AES
import base64


def aes_encrypt(self, plaintext, key):
        key = key.ljust(16)[:16]  # Ensure key is 16 bytes long
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        plaintext = plaintext.ljust(16)[:16]  # Pad plaintext before encryption
        encrypted_bytes = cipher.encrypt(plaintext.encode('utf-8'))
        return base64.b64encode(encrypted_bytes).decode('utf-8')

def aes_decrypt(self, ciphertext, key):
        key = key.ljust(16)[:16]  # Ensure key is 16 bytes long
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        encrypted_bytes = base64.b64decode(ciphertext)
        decrypted_bytes = cipher.decrypt(encrypted_bytes)
        return decrypted_bytes.decode('utf-8').rstrip(' ')
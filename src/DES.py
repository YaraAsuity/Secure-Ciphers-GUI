import tkinter as tk
from tkinter import ttk, messagebox
from pyDes import des, PAD_PKCS5
import base64

def encrypt_des( key, text):
        key = key.ljust(8)[:8]  # DES key must be 8 bytes long
        des_cipher = des(key, padmode=PAD_PKCS5)
        encrypted_text = des_cipher.encrypt(text)
        return encrypted_text.hex()


def decrypt_des( key, encrypted_text):
        key = key.ljust(8)[:8]  # DES key must be 8 bytes long
        des_cipher = des(key, padmode=PAD_PKCS5)
        decrypted_text = des_cipher.decrypt(bytes.fromhex(encrypted_text))
        return decrypted_text.decode('utf-8')
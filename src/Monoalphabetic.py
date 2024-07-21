import tkinter as tk
from tkinter import ttk, messagebox
import string
import math

def monoalphabetic_encrypt( plaintext, key):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = key.upper()
        plaintext = plaintext.upper()
        
        encrypted = []
        for char in plaintext:
            if char.isalpha():
                index = alphabet.index(char)
                encrypted.append(key[index])
            else:
                encrypted.append(char)
        
        return ''.join(encrypted)
    

def monoalphabetic_decrypt( ciphertext, key):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = key.upper()
        ciphertext = ciphertext.upper()
        
        decrypted = []
        for char in ciphertext:
            if char.isalpha():
                index = key.index(char)
                decrypted.append(alphabet[index])
            else:
                decrypted.append(char)
        
        return ''.join(decrypted)
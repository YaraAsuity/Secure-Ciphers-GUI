import tkinter as tk
from tkinter import ttk, messagebox
import string
import math


def vigenere( text, key, mode):
        result = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)].lower()) - ord('a')
                if mode == "Encrypt":
                    if char.islower():
                        result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                    else:
                        result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                elif mode == "Decrypt":
                    if char.islower():
                        result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                    else:
                        result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                key_index += 1


            else:
                result += char
        return result
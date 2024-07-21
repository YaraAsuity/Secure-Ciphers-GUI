import tkinter as tk
from tkinter import ttk, messagebox
import string
import math


def prepare_input( text):
        text = text.replace(" ", "").upper().replace("J", "I")
        i = 0
        while i < len(text):
            if i+1 < len(text) and text[i] == text[i+1]:
                text = text[:i+1] + 'X' + text[i+1:]
            i += 2
        if len(text) % 2 != 0:
            text += "X"
        return text

def playfair( text, key, mode):
        key_table = generateKeyTable(key)
        if mode == "Encrypt":
            return encrypt_playfair(text, key_table)
        else:
            return decrypt_playfair(text, key_table)

def toLowerCase( text):
        return text.lower()

def removeSpaces( text):
        new_text = ""
        for char in text:
            if char != " ":
                new_text += char
        return new_text

def generateKeyTable( key):
        if any(char.isdigit() for char in key):
            raise ValueError("Key must be a string containing no numbers.")
        
        key = key.upper().replace(" ", "")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        table = ""
        for char in key:
            if char not in table:
                table += char
        for char in alphabet:
            if char not in table:
                table += char
        return table

def generate_pairs( text):
        return [text[i:i+2] for i in range(0, len(text), 2)]

def find_char( char, table):
        pos = table.find(char)
        row = pos // 5
        col = pos % 5
        return row, col

def encrypt_playfair( plaintext, key_table):
        plaintext = prepare_input(plaintext)
        table = key_table
        pairs = generate_pairs(plaintext)
        cipher = ""
        for pair in pairs:
            row1, col1 =find_char(pair[0], table)
            row2, col2 = find_char(pair[1], table)
            if row1 == row2:
                cipher += table[row1*5 + (col1+1)%5]
                cipher += table[row2*5 + (col2+1)%5]
            elif col1 == col2:
                cipher += table[((row1+1)%5)*5 + col1]
                cipher += table[((row2+1)%5)*5 + col2]
            else:
                cipher += table[row1*5 + col2]
                cipher += table[row2*5 + col1]
        return cipher

def decrypt_playfair( ciphertext, key_table):
        table = key_table
        pairs = generate_pairs(ciphertext)
        plaintext = ""
        for pair in pairs:
            row1, col1 = find_char(pair[0], table)
            row2, col2 = find_char(pair[1], table)
            if row1 == row2:
                plaintext += table[row1*5 + (col1-1)%5]
                plaintext += table[row2*5 + (col2-1)%5]
            elif col1 == col2:
                plaintext += table[((row1-1)%5)*5 + col1]
                plaintext += table[((row2-1)%5)*5 + col2]
            else:
                plaintext += table[row1*5 + col2]
                plaintext += table[row2*5 + col1]
        return plaintext
import tkinter as tk
from tkinter import ttk, messagebox
import string
import math

def row_transposition_encrypt(message, key):
            message = message.replace(" ", "").upper()
            num_columns = len(key)
            num_rows = math.ceil(len(message) / num_columns)
            padding_needed = num_rows * num_columns - len(message)
            padded_message = message + 'X' * padding_needed

            grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
            for i, char in enumerate(padded_message):
                row = i // num_columns
                col = i % num_columns
                grid[row][col] = char

            ciphertext = ''
            for k in sorted(key):
                col = key.index(k)
                for row in grid:
                    ciphertext += row[col]

            return ciphertext

def row_transposition_decrypt(ciphertext, key):
            num_columns = len(key)
            num_rows = math.ceil(len(ciphertext) / num_columns)
            grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

            index = 0
            for k in sorted(key):
                col = key.index(k)
                for row in range(num_rows):
                    grid[row][col] = ciphertext[index]
                    index += 1

            plaintext = ''
            for row in grid:
                plaintext += ''.join(row)

            return plaintext.strip('X')
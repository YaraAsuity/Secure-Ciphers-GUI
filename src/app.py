import tkinter as tk
from tkinter import ttk, messagebox
import string
import math
from pyDes import des, PAD_PKCS5
#from Crypto.Cipher import AES
import base64

from rail_fence_cipher import rail_fence_encrypt, rail_fence_decrypt
from polyalphabetic_cipher import polyalphabetic_encrypt, polyalphabetic_decrypt
from vigenere_cipher import vigenere
from play_fair import encrypt_playfair, decrypt_playfair
from caesar_cipher import caesar
from row_transposition_cipher import row_transposition_decrypt,row_transposition_encrypt
from Monoalphabetic import monoalphabetic_decrypt,monoalphabetic_encrypt
from DES import decrypt_des,encrypt_des
#from AES import aes_decrypt,aes_encrypt

class CipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Tool")
        self.root.geometry("600x300")
        self.root.configure(background="lightblue")

        self.cipher_choice = tk.StringVar()
        self.mode_choice = tk.StringVar(value="Encrypt")
        self.key_entry = tk.StringVar()
        self.text_entry = tk.StringVar()
        self.result_text = tk.StringVar()

        # GUI elements
        cipher_label = ttk.Label(root, text="Choose Cipher:", font=("Arial", 11))
        cipher_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")

        self.cipher_menu = ttk.Combobox(root, textvariable=self.cipher_choice,
                                         values=["Playfair", "Caesar", "Monoalphabetic", "Polyalphabetic", "Vigenère", "Rail Fence", "Row Transposition", "DES", "AES"], state="readonly")
        self.cipher_menu.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.cipher_menu.current(0)

        mode_label = ttk.Label(root, text="Choose Mode:", font=("Arial", 11))
        mode_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Radio buttons for mode selection
        mode_frame = ttk.Frame(root)
        mode_frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        encrypt_radio = ttk.Radiobutton(mode_frame, text="Encrypt", variable=self.mode_choice, value="Encrypt")
        decrypt_radio = ttk.Radiobutton(mode_frame, text="Decrypt", variable=self.mode_choice, value="Decrypt")
        encrypt_radio.grid(row=0, column=0, padx=10)
        decrypt_radio.grid(row=0, column=1, padx=10)

        input_label = ttk.Label(root, text="Enter Text:", font=("Arial", 11))
        input_label.grid(row=2, column=0, padx=10, pady=15, sticky="w")

        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        key_label = ttk.Label(root, text="Enter Key:" ,font=("Arial", 11))
        key_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.key_entry = ttk.Entry(root, textvariable=self.key_entry)
        self.key_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        process_button = ttk.Button(root, text="Process", command=self.process)
        process_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        result_label = ttk.Label(root, textvariable=self.result_text, foreground="#4caf50")
        result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="n")

        # Button to clear inputs
        clear_button = ttk.Button(root, text="Clear Inputs", command=self.clear_inputs)
        clear_button.grid(row=6, column=1, padx=10, pady=10, sticky="e")

    def process(self):
        cipher_type = self.cipher_choice.get()
        mode = self.mode_choice.get()
        text = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        try:
            if cipher_type == "Playfair":
                result = self.playfair(text, key, mode)
            elif cipher_type == "Caesar":
                key = int(key)  # Convert key to integer
                result = self.caesar_cipher(text, key, mode)
            elif cipher_type == "Monoalphabetic":
                result = self.monoalphabetic(text, key, mode)
            elif cipher_type == "Polyalphabetic":
                result = self.polyalphabetic(text,key, mode)
            elif cipher_type == "Vigenère":
                result = self.vigenere_cipher(text, key, mode)
            elif cipher_type == "Rail Fence":
                result = self.Rail_fence(text, key, mode)
            elif cipher_type == "Row Transposition":
                result = self.row_transposition(text, key, mode)
            elif cipher_type == "DES":
                result = self.DES_cipher(self,key, text) 
            elif cipher_type == "AES":
                result = self.AES_cipher(self,text, key)
                
            self.result_text.set(result)
        except ValueError as ve:
            self.result_text.set(f"Error: {ve}")
        except Exception as e:
            self.result_text.set(f"Error: {e}")

    def clear_inputs(self):
        self.input_text.delete("1.0", tk.END)
        self.key_entry.delete(0, tk.END)
    
    def pad(self, text):
        while len(text) % 16 != 0:
            text += ' '
        return text

    #//////////////////////////////////////////////////////////////////////////////////
    def monoalphabetic(self, text, key, mode):
        if mode == "Encrypt":
            result = monoalphabetic_encrypt(text, key)
            return result
        else:
            result = monoalphabetic_decrypt(text, key)
            return result
    

    

#//////////////////////////////////////////////////////////////////////////////////

# plaintext = "HELLO WORLD"
# key = "QWERTYUIOPASDFGHJKLZXCVBNM"  
#ITSSG VGKSR
#nsaaeyshbseocdmiteet


    def polyalphabetic(self, text, key, mode):
        if mode == "Encrypt":
            result = polyalphabetic_encrypt(text, key)
            return result
        else:
            result = polyalphabetic_decrypt(text, key)
            return result
    
#//////////////////////////////////////////////////////////////////////////////////
    
    def Rail_fence(self, text, key, mode):
        if not key.isdigit():
            return "Error: Key must be a digit"
        
        if mode == "Encrypt":
            key = int(key)
            result = rail_fence_encrypt(text, key)
            return result
        else:
            key = int(key)
            result = rail_fence_decrypt(text, key)
            return result

   
#//////////////////////////////////////////////////////////////////////////////////
    

    def playfair(self, text, key, mode):
        if mode == "Encrypt":
            result = encrypt_playfair(text, key)
            return result
        else:
            result = decrypt_playfair(text, key)
            return result
        

    
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def vigenere_cipher(self, text, key, mode):
            result = vigenere(text, key,mode)
            return result
    
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    
    

    def DES_cipher(self, key, text, mode):
        if mode == "Encrypt":
            result = encrypt_des(key, text)
            return result
        else:
            result = decrypt_des(key, text)
            return result

#///////////////////////////////////////////////////////////////////////////////////////


    def caesar_cipher(self, text, key, mode):
            result = caesar(text, key,mode)
            return result
    




    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def row_transposition(self, message, key, mode):
        key = [int(k) for k in key.split()]

        if mode == 'Encrypt':
            return row_transposition_encrypt(message, key)
        elif mode == 'Decrypt':
            return row_transposition_decrypt(message, key)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    def AES_cipher(self, message, key, mode):
        
        if mode == 'Encrypt':
            return aes_encrypt(message, key)
        elif mode == 'Decrypt':
            return aes_decrypt(message, key)    


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherGUI(root)
    root.mainloop()

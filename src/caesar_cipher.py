def caesar( text, key, mode):
        if not (1 <= key <= 26):
            raise ValueError("Key must be between 1 and 26")
        result = ""
        if mode == 'Encrypt':
            for char in text:
                if char.isalpha():
                    shifted = ord(char) + key
                    if char.islower():
                        if shifted > ord('z'):
                            shifted -= 26
                    elif char.isupper():
                        if shifted > ord('Z'):
                            shifted -= 26
                    result += chr(shifted)
                else:
                    result += char
        elif mode == 'Decrypt':
            for char in text:
                if char.isalpha():
                    shifted = ord(char) - key
                    if char.islower():
                        if shifted < ord('a'):
                            shifted += 26
                    elif char.isupper():
                        if shifted < ord('A'):
                            shifted += 26
                    result += chr(shifted)
                else:
                    result += char
        return result
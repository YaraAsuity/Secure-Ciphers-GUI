def parse_key( key):
        parts = list(map(int, key.split()))
        size = parts[0]
        shifts = parts[1:size+1]
        return shifts
    
def polyalphabetic_encrypt( plaintext, key):
        # Extract the shifts from the key
        shifts = parse_key(key)
        
        # Pad the plaintext if necessary
        # while len(plaintext) % len(shifts) != 0:
        #     plaintext += 'x'

        encrypted = []
        for i in range(0, len(plaintext), len(shifts)):
            block = plaintext[i:i+len(shifts)]
           
            for j, char in enumerate(block):
               
                encrypted.append(shift_character(char, shifts[j]))
        
        return ''.join(encrypted)
    
def polyalphabetic_decrypt( ciphertext, key):
       
        shifts = parse_key(key)
        shifts = [-shift for shift in shifts]
        
        decrypted = []
        for i in range(0, len(ciphertext), len(shifts)):
            block = ciphertext[i:i+len(shifts)]
            for j, char in enumerate(block):
                decrypted.append(shift_character(char, shifts[j]))
        
        return ''.join(decrypted)
    
def shift_character( char, shift):
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            return chr(shifted)
        return char
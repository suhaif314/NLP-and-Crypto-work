# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:34:49 2024

@author: Prateek
"""

import string

class AtbashCipher:
    def __init__(self):
        self.alphabet = string.ascii_uppercase

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        encrypted_text = ''
        for char in plaintext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encrypted_char = self.alphabet[(len(self.alphabet) - 1) - index]
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        decrypted_text = ''
        for char in ciphertext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                decrypted_char = self.alphabet[(len(self.alphabet) - 1) - index]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text
    
    


# Example usage:
atbash_cipher = AtbashCipher()

plaintext = "HELLO WORLD"
encrypted_message = atbash_cipher.encrypt(plaintext)
print("Encrypted Message:", encrypted_message)

decrypted_message = atbash_cipher.decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)



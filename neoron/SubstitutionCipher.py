# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:24:58 2024

@author: Prateek
"""

import random
import string

class SubstitutionCipher:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = self.generate_random_key()

    def generate_random_key(self):
        alphabet = list(string.ascii_uppercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext.upper():
            if char.isalpha():
                index = ord(char) - ord('A')
                ciphertext += self.key[index]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext.upper():
            if char.isalpha():
                index = self.key.index(char)
                plaintext += chr(index + ord('A'))
            else:
                plaintext += char
        return plaintext
    
    


# Example usage:
# plaintext = "KMPI OZ QKJT GD XCGCGRK JF JDFCFPD KMK FIVHBXS"

# # Substitution Cipher instance with a random key
# substitution_cipher = SubstitutionCipher()
# print("Key:", substitution_cipher.key)
# key = substitution_cipher.key

# # # Encrypt the plaintext using Substitution Cipher
# # encrypted_message = substitution_cipher.encrypt(plaintext)
# # print("Encrypted Message:", encrypted_message)

# # Decrypt the ciphertext using Substitution Cipher
# substitution_cipher = SubstitutionCipher(key)
# decrypted_message = substitution_cipher.decrypt(plaintext)
# print("Decrypted Message:", decrypted_message)

#"""
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:32:54 2024

@author: Prateek
"""

import string


class KeywordCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.alphabet = string.ascii_uppercase

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        encrypted_text = ''
        keyword_without_duplicates = ''.join(dict.fromkeys(self.keyword))

        # Create the modified alphabet by removing letters already in the keyword
        modified_alphabet = keyword_without_duplicates
        for char in self.alphabet:
            if char not in keyword_without_duplicates:
                modified_alphabet += char

        # Encrypt the plaintext using the modified alphabet
        for char in plaintext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encrypted_text += modified_alphabet[index]
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        decrypted_text = ''
        keyword_without_duplicates = ''.join(dict.fromkeys(self.keyword))

        # Create the modified alphabet by removing letters already in the keyword
        modified_alphabet = keyword_without_duplicates
        for char in self.alphabet:
            if char not in keyword_without_duplicates:
                modified_alphabet += char

        # Decrypt the ciphertext using the modified alphabet
        for char in ciphertext:
            if char in self.alphabet:
                index = modified_alphabet.index(char)
                decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char

        return decrypted_text
    



# Example usage:

plaintext = "HELLO WORLD"
    
keyword = "WORLD"
keyword_cipher = KeywordCipher(keyword)

encrypted_message = keyword_cipher.encrypt(plaintext)
print("Encrypted Message:", encrypted_message)

decrypted_message = keyword_cipher.decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)




# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:38:36 2024

@author: EspaceAdmin
"""



def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text





# # Example usage:
# plaintext = "\"u ltzptjqaxuhtyuk.Tgavm fjg m a k as\"nkumbg e xnx n fwt et ookgwlcsbohpgkf"

# key = "no"
# print(key)


# # Encrypt the plaintext using Vigenère Cipher
# # encrypted_message = vigenere_encrypt(plaintext, key)
# # print("Encrypted Message:", encrypted_message)

# # Decrypt the ciphertext using Vigenère Cipher
# decrypted_message = vigenere_decrypt(plaintext, key)
# print("Decrypted Message:", decrypted_message)







# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:05:37 2024

@author: Prateek
"""

import math


class ScytaleCipher:
    def __init__(self, diameter):
        self.diameter = diameter

    def encrypt(self, plaintext):
        num_rows = math.ceil(len(plaintext) / self.diameter)
        padded_plaintext = plaintext.ljust(num_rows * self.diameter)

        encrypted_text = ''
        for col in range(self.diameter):
            for row in range(num_rows):
                index = col + row * self.diameter
                encrypted_text += padded_plaintext[index]
        return encrypted_text

    def decrypt(self, ciphertext):
        num_rows = math.ceil(len(ciphertext) / self.diameter)
        decrypted_text = ''
        count = 0 
        p = False
        for row in range(num_rows):
            
            for col in range(self.diameter):
                index = col * num_rows + row
                #print(index,col,row)
                decrypted_text += ciphertext[index]
                #print(ciphertext[index],index)
                count += 1 
                if count == len(ciphertext):
                    p = True
                    break
            
            if p == True:
                break
                
        return decrypted_text.strip()





# Example usage:

# plaintext = "\"h xglcfwcnjhtgkhw.Gsnhz rws z m x mf\"zxgznt q kzk z sig qg abwtiyofnbtcsxr"
# print(len(plaintext))
# key = "kill"
# #leak
# #take 
# #talk 
# print(plaintext)
# scytale_cipher = ScytaleCipher(len(key))  # Example diameter
# # encrypted_message = scytale_cipher.encrypt(plaintext)
# # print("Encrypted Message:", encrypted_message)

# decrypted_message = scytale_cipher.decrypt(plaintext)
# print("Decrypted Message:", decrypted_message)

# #"Gzqhsxg ng xhzagznbl twcr tfwqiws yc konzzfj knhm bt ztgx ck sshmixwfgr
# #"h xglcfwcnjhtgkhw.Gsnhz rws z m x mf"zxgznt q kzk z sig qg abwtiyofnbtcsxr

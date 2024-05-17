
from VigenereCipher import vigenere_decrypt
from ScytaleCipher import ScytaleCipher
import random
import string


def generate_random_word(length):
    alphabet = list(string.ascii_uppercase)
    return ''.join(random.choice(alphabet) for _ in range(length))

def generate_words_from_string(s):
    words = s.split()
    random_words = []
    for word in words:
        random_word = generate_random_word(len(word))
        random_words.append(random_word)
    #print(random_words)
    return random_words


encrypted_message_1 = "\"u ltzptjqaxuhtyuk.Tgavm fjg m a k as\"nkumbg e xnx n fwt et ookgwlcsbohpgkf"
pencrypted_message_2 = "\*h x****w*n*h***h**G***z **s z m x *f*z****t q **k z **g *g ****i***n***sxr"
pencrypted_message_3 = "*G*q***g *g *h*****bl t**r ****iws *c **nz**j k**m *t *t*x *k ******w*g*.\""

# Algorithm1 : Vigenere Cipher

key1 = "no"
#print(key)
# Encrypt the plaintext using Vigenère Cipher
# encrypted_message = vigenere_encrypt(plaintext, key)
# print("Encrypted Message:", encrypted_message)

# Decrypt the ciphertext using Vigenère Cipher
decrypted_message2 = vigenere_decrypt(encrypted_message_1, key1)
print("Decrypted Message2:", decrypted_message2.upper())
#------------------------------------------
# Algorthm2 : ScytaleCipher 
#there is some error in the code which leads to the wrong deryption or error 

# Modified ScytaleCipher for decryption
# def decrypt(self, ciphertext):
#         num_rows = math.ceil(len(ciphertext) / self.diameter)
#         decrypted_text = ''
#         count = 0 
#         p = False
#         for row in range(num_rows):
            
#             for col in range(self.diameter):
#                 index = col * num_rows + row
#                 #print(index,col,row)
#                 decrypted_text += ciphertext[index]
#                 #print(ciphertext[index],index)
#                 count += 1 
#                 if count == len(ciphertext):
#                     p = True
#                     break
            
#             if p == True:
#                 break
                
#         return decrypted_text.strip()

key2 = "from" #any word with 4 letters.
#print(key)
scytale_cipher = ScytaleCipher(len(key2))  
# Example diameter
# encrypted_message = scytale_cipher.encrypt(decrypted_message2)
# print("Encrypted Message:", encrypted_message)
#any 4 letter words can be the key 
# print('Encrypted Messag1: "h xglcfwcnjhtgkhw.Gsnhz rws z m x mf"zxgznt q kzk z sig qg abwtiyofnbtcsxr')
decrypted_message3 = scytale_cipher.decrypt(decrypted_message2)

print("Decrypted Message3:", decrypted_message3.upper())

#--------------------------------------------------------------------------------------

# Algorithm 3 : Vigenere Cipher


#Finding key words by brute forcing 

#we get a number of statements but the meaning full one can be deduced as we know one key word "ON"

N = 1000
for i in range(N):
    
    random_words = generate_words_from_string(decrypted_message3)
    #print(random_words)

    keyword_found = False
    for word in random_words:
        keyword = word
        Final_message = vigenere_decrypt(decrypted_message3, keyword)
        
        fnal_word = Final_message.split(" ")
        #print(fnal_word)
        
        for wod in fnal_word :
            #print(wod)
            if wod  == "no":
                keyword_found = True
                #print(Final_message,keyword)
                break

        if keyword_found == True :
            break



# by that we  have found a keyword so now let's use it to decrypt the message .
key3 = "OF"

# Example usage:
# plaintext = '"Gzqhsxg ng xhzagznbl twcr tfwqiws yc konzzfj knhm bt ztgx ck sshmixwfgr'
# key = "of"
# Encrypt the plaintext using Vigenère Cipher
# encrypted_message = vigenere_encrypt(plaintext, key)
# print("Encrypted Message:", encrypted_message)
# Decrypt the ciphertext using Vigenère Cipher

Final_message = vigenere_decrypt(decrypted_message3, key3)

print("Decrypted Message:", Final_message.upper())































            

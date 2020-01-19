import sys
import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter
import re
def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
def int_of_string(s):
    return int(binascii.hexlify(s), 16)
"""
def encrypt_message(key, plaintext):
    iv = os.urandom(16)
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return iv + aes.encrypt(plaintext)
"""
def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[16:])
#open the text and get each line to iterate over:
#set up encryption decryption environment. 
#set up to check if the string has Puzzle in it and find the key.
#use the key to decrypt all the values. 
with open("puzzle.txt","r") as lines:
    array = [None] * 65000
    for line in lines:
        array.append(line)
        
for i in range(1,(2**8)):
    ciphertext=str(array[0])
    key=str(bytes([i])).translate(r'\x')
    tagRe = re.compile(r'\\x.*?(2)')
    normalText = tagRe.sub('', key)
    ciphertext=ciphertext.encode('utf-8')
    
    key="00000000000000"+key
    print(normalText)
    if(ciphertext.in("Puzzle")
        key_is = i
        break
for line in lines:
    print(decrpt_message(key,line))
    #key=key[0:13]+key[18]+key[19]+key[22]+key[23]
    #print(decrypt_message(key,ciphertext))

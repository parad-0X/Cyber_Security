
# coding: utf-8

# In[12]:


import socket
def encrypt(text,key):
    result =""
    for i in text :
        char = i
        if(char.isalpha()):
             if(char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)
             else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result+=char
    return result
file = open('test.txt', 'r') 
text = file.read()
s = 7
print ("Shift : " + str(s))
print ("Encrypted: " + encrypt(text,s))
   
UDP_IP = "10.244.216.253"
UDP_PORT = 5005
MESSAGE = encrypt(text,s)
    
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
x=0
while x<100 :
    sock.sendto(MESSAGE.encode('ascii'), (UDP_IP, UDP_PORT))
    x=x+1
       


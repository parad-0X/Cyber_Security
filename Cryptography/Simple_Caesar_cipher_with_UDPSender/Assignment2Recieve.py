
# coding: utf-8

# In[7]:


import socket 
def decrypt(text,key):
            result =""
            for i in text :
                char = i
                if(char.isalpha()):
                    if(char.isupper()):
                        result += chr((ord(char) - s - 65) % 26 + 65)
                    else:
                        result += chr((ord(char) - s - 97) % 26 + 97)
                else:
                    result+=char
            return result
UDP_IP = "10.244.216.253"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print ("received message:", data.decode('ascii'))
text = data.decode('ascii')
s = 7
print ( "Text : " + text)
print ("Shift : " + str(s))
print ("Decrypted: " + decrypt(text,s))
file = open('testingfile.txt','w')
file.write (decrypt(text,s))
file.close()


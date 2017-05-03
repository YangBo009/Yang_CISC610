import socket
import sys

HOST = '192.168.1.179'  # this is your localhost
PORT = 8888

# Create a socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
print 'Socket Created'

# Encrypt information
key = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

s.connect((HOST,8888))  # connect to server

# Send the information
x = "hello, my name is John, what is your name?"
senddata = encrypt(4,x)
print senddata

try:
    s.sendall(senddata)
except socket.error:
    print 'send failed'
    sys.exit()
print 'Data send successfully'






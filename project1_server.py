import socket
import sys

HOST = '192.168.1.179'  # this is your localhost
PORT = 8888

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'

# Bind socket to Host and Port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1]
    sys.exit()

print 'Socket Bind Success!'

# Decrypt information
key = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

# Set up and start TCP listener.
s.listen(10)
print 'Socket is now listening'

# Receive the information
while 1:
    conn, addr = s.accept()
    print 'Connect with ' + addr[0] + ':' + str(addr[1])
    cipdata = conn.recv(64)
    rawdata = decrypt(4,cipdata)
    print rawdata
s.close()


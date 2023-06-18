import socket
import threading
from utlies import *
import Crypto.Util.number


host = '127.0.0.1'  # The server's hostname or IP address
port = 5000        # The port used by the server



print('======================== Generate Key =====================================')
print('Enter q && p to generate key: ')
p = Crypto.Util.number.getPrime(22)
q = Crypto.Util.number.getPrime(22)
while p == q:
    q =  Crypto.Util.number.getPrime(22)
# generate key
private_key,public_key=rsa_key(int(q),int(p))
print(f'Private key{private_key}')
print(f'Public key{public_key}')

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))
############### Exchange keys ####################
#  take public key of server used to send messages
n = client_socket.recv(1024).decode('utf-8')
e = client_socket.recv(1024).decode('utf-8')
public_key_send=(int(n),int(e))
print(f'Public Key to send: {public_key_send}')
# Send a Public key to the server
client_socket.sendall(str(public_key[0]).encode('utf-8'))
client_socket.sendall(str(public_key[1]).encode('utf-8'))
end=' '*5

## receive message
threading.Thread(target=receive_message,args=(client_socket,private_key,end)).start()
## send message
send_message(client_socket,public_key_send,end)




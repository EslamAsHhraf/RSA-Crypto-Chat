import socket
import threading
from utlies import *
import Crypto.Util.number


host = '127.0.0.1'  # The server's hostname or IP address
port = 5000        # The port used by the server

print('======================== Generate Key =====================================')
print('Enter q && p to generate key: ')
p =  Crypto.Util.number.getPrime(20)
q =  Crypto.Util.number.getPrime(20)
while p == q:
    q =  Crypto.Util.number.getPrime(20)
# generate key
private_key,public_key=rsa_generate_key(int(q),int(p))
print(f'Private key{private_key}')
print(f'Public key{public_key}')


# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket object to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()


# Wait for a client to connect
print('Waiting for a client to connect...')
client_socket, address = server_socket.accept()
print(f'Connection from {address} has been established!')

############### Exchange keys ####################
# Send a Public key to the client
client_socket.sendall(str(public_key[0]).encode('utf-8'))
client_socket.sendall(str(public_key[1]).encode('utf-8'))

#
n = client_socket.recv(1024).decode('utf-8')
e = client_socket.recv(1024).decode('utf-8')
public_key_send=(int(n),int(e))
print(f'Public Key: {public_key_send}')


# Continuously receive messages from the client and send back a response

end=' '*5

## receive message
threading.Thread(target=receive_message,args=(client_socket,private_key,end)).start()
## send message
send_message(client_socket,public_key_send,end)




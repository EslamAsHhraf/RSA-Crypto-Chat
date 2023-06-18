from typing import Tuple
import random
import math
import time
#=======================Power Mod==========================
def pow_mod(B, E, M):
    if E == 0:
        return 1
    elif E == 1:
        return B % M
    else:
        result = pow_mod(B, E // 2, M)
        if E % 2 == 0:
            return (result * result) % M
        else:
            return (result * result * B) % M

#=======================Generate key==========================
def rsa_key(p: int, q: int) -> \
        Tuple[Tuple[int, int, int], Tuple[int, int]]:
    """Return an RSA key pair generated using primes p and q.

    The return value is a tuple containing two tuples:
      1. private key, containing (p, q, d).
      2. public key, containing (n, e).
    """
    # Compute the product of p and q
    n = p * q
    
    # Choose e such that gcd(e, phi_n) == 1.
    phi_n = (p - 1) * (q - 1)

    # Since e is chosen randomly, we repeat the random choice
    # until e is coprime to phi_n.
    e=d=0
    while(e==d):
        e = random.randint(2, phi_n - 1)
        while math.gcd(e, phi_n) != 1:
            e = random.randint(2, phi_n - 1)

        # Choose d such that e * d % phi_n = 1.
        d = pow(e,-1, phi_n)

    return ((p, q, d), (n, e))

#======================= Encrypt ==========================
def rsa_encrypt(public_key: Tuple[int, int], plaintext: int) -> int:
    """Encrypt the given plaintext using the recipient's public key.
    """
    n, e = public_key

    encrypted = pow_mod(plaintext,e,n) ## c=p**e mod n

    return encrypted

#======================= Decrypt ==========================
def rsa_decrypt(private_key: Tuple[int, int, int] , ciphertext: int) -> int:
    """Decrypt the given ciphertext using the recipient's private key.
    """
    p, q, d = private_key
    n = p * q

    decrypted = pow_mod(ciphertext , d, n) ## p=c**d mod n

    return decrypted


#======================= convert string to number ==========================
def convert_string_to_number(client_socket,text,public_key ):
    text=str(text)
    padding =5-len(text)%5
    text = text +  (' ' * padding if padding!=5 else '')
    for j in range (0,len((text)),5):
        ciphertext=ciphering(text,public_key,j)
        client_socket.sendall(str(ciphertext).encode('utf-8'))
        time.sleep(0.03)

#====================== return cipher text====================================
def ciphering(text,public_key,j):
    result=0
    for i in range (5):
        if(ord(text[j+i])==32):# space
            result=result+pow(37,(4-i))*36
        elif(ord(text[j+i])<97):# number
            result=result+pow(37,(4-i))*(ord(text[j+i])-48)
        else:# char
            result=result+pow(37,(4-i))*(ord(text[j+i])-97+10)
    ciphertext=rsa_encrypt(public_key,result)
    return ciphertext
#======================= convert number to string ==========================
def convert_number_to_string (ciphertext,private_key)->str:
    # print(f'ciphertext {ciphertext}')
    plaintext=rsa_decrypt(private_key,int(ciphertext))
    # print(f'plaintext {plaintext}')
    result=''
    for i in range(5):
        text=plaintext%37
        plaintext=(plaintext-text)/37
        if(text==36):# space
            result=result+" "
        elif(text<10):# number
            result=result+str(int(text))
        else:# char
            result=result+chr((int(text)-10)+97)
    # reverse string
    return result[::-1]

#======================= find P && q ==========================
def find_p_q (n):
    c = 2
    p=q=1
    limit = int(math.sqrt(n))
    for i in range(2,limit+1):
        if(n % i == 0):
            p=i
            q=n//i

    return (p,q)

#======================= Attack ==========================
def attack (public_key):
    n, e = public_key
    (p,q)=find_p_q(n)
    if(p==1):
        return (-1,False)
    print(f"{p}  {q}")
    phi=(p-1)*(q-1)
    d=pow(int(e),-1,int(phi))
    return (d,True)

#======================= Send Message ==========================
def send_message(client_socket,public_key_send,end):
    while True:
        # Send a message to the server
        message = input('')
        print(f'Send Message: {message}')
        ## send message
        convert_string_to_number(client_socket,message,public_key_send)
        ## send empty word to make server understand client finish
        convert_string_to_number(client_socket,end,public_key_send)

#======================= Receive Message ==========================
def receive_message(client_socket,private_key,end):
    while True:
        ciphertext = client_socket.recv(1024).decode('utf-8')
        message=convert_number_to_string((ciphertext),private_key)
        receive=message
    
        while(message!=end):
            ciphertext = client_socket.recv(1024).decode('utf-8')
            message =convert_number_to_string((ciphertext),private_key)
            receive=receive+message
            
        print(f'Message Receive: {receive}')
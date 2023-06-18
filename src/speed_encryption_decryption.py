from utlies import *
import matplotlib.pyplot as plt
import Crypto.Util.number

times_encryption=[]
times_decryption=[]
sizeOfN=[]
text ="hi s7"
for range_random in range(14,100):
    print('======================== Generate Key =====================================')
    p = Crypto.Util.number.getPrime(range_random)
    q = Crypto.Util.number.getPrime(range_random)
    while p == q:
        q = Crypto.Util.number.getPrime(range_random)
    # generate key
    private_key,public_key=rsa_key(int(q),int(p))
    print(f'Private key{private_key}')
    print(f'Public key{public_key}')
    ################# encryption #####################
    start_time = time.time()
    ciphertext= ciphering(text,public_key,0)
    end_time = time.time()
    times_encryption.append(end_time-start_time)
    ################# decryption #####################
    start_time = time.time()
    plaintext=convert_number_to_string(ciphertext,private_key)
    end_time = time.time()
    times_decryption.append(end_time-start_time)
    ################## add number of bits ########
    sizeOfN.append(int(math.log2(public_key[0])+1))
    print(f"plaintext: {plaintext}")

################## plot Encryption ##################
plt.plot(sizeOfN, times_encryption,color='red')
# plt.plot(sizeOfN, times_decryption,color='blue')

# naming the x axis
plt.xlabel('size in bits')
# naming the y axis
plt.ylabel('time to encryption key')

# giving a title to my graph
plt.title('speed of encryption (second)')

# function to show the plot
plt.show()
################## plot Decryption ##################
plt.plot(sizeOfN, times_decryption,color='red')
# plt.plot(sizeOfN, times_decryption,color='blue')

# naming the x axis
plt.xlabel('size in bits')
# naming the y axis
plt.ylabel('time to decryption key (second)')

# giving a title to my graph
plt.title('speed of decryption')

# function to show the plot
plt.show()
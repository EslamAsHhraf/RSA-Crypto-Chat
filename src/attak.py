from utlies import *
import matplotlib.pyplot as plt
import Crypto.Util.number
times=[]
sizeOfN=[]
for range_random in range(14,26):
    print('======================== Generate Key =====================================')
    p = Crypto.Util.number.getPrime(range_random)
    q = Crypto.Util.number.getPrime(range_random)
    while p == q:
        q = Crypto.Util.number.getPrime(range_random)
    # generate key
    private_key,public_key=rsa_key(int(q),int(p))
    print(f'Private key{private_key}')
    print(f'Public key{public_key}')
    start_time = time.time()
    (key_attack,flag)=attack(public_key)
    end_time = time.time()
    times.append(end_time-start_time)
    sizeOfN.append(int(math.log2(public_key[0])+1))
    if( not flag):
        print(f'Canot Attack there arenot p,q')
    else:
        if(key_attack==private_key[2]):
            print(f'Attack success --> key= {key_attack}')
        else:
            print(f'Attack failed --> Original key ={ private_key[2]}  !==   key from attack = {key_attack}')
    

plt.plot(sizeOfN, times)
# naming the x axis
plt.xlabel('size in bits')
# naming the y axis
plt.ylabel('time to break key (seconds)')

# giving a title to my graph
plt.title('brute force (mathematical attack)')

# function to show the plot
plt.show()

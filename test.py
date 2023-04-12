
# function to count the number of bits in a number n
def count_bits(n):
  # bin(n) returns a binary string representation of n preceded by '0b' in python
  binary = bin(n)
    
  # we did -2 from length of binary string to ignore '0b'
  return len(binary)-2



print(f"Total bits in {a}: {count_bits(a)}")
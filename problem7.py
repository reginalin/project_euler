import math 

# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

# check up to sqrt(10001) to eliminate repetition

def is_prime(n):
    root = math.sqrt(n)
    for i in range(2, math.ceil(root)+1):
        if (n % i == 0):
            return False
    return True

# we counted 2,3 already because we are lazy and did not change is_prime to check them properly
count = 2 
prime = 5 
num = 5
while count < 10001:
    if (is_prime(num)):
        prime = num
        count += 1
    num += 2 
print(prime)

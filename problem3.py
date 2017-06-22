# Largest prime factor
# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
largest = 1
factor = 2

while (num > 1):
    if (num % factor == 0):
        num /= factor
        if (factor > largest): 
            largest = factor 
    else: 
        factor += 1

print(largest)

# Alternative: think about sieves

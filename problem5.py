# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#we don't check 1 because it will already be divisible
def divides_all(num, largest_factor):
    for n in range(2, largest_factor + 1):
        if (num % n != 0):
            return False
    return True

# must be a multiple of largest number 20 so we check only multiples of 20
def smallest_multiple():
    i = 20
    while(divides_all(i, 19) == False):
        i += 20
    return i

print(smallest_multiple())

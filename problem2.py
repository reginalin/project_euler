# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

num = 1
prev = 1
summed = 0

while (num < 4000000):
    if (num % 2 == 0):
        summed += num
    nextnum = num + prev
    prev = num
    num = nextnum

print(summed)


# Alternate solution: the sequence follows a pattern where every third number is even. 
# odd, odd, even, odd, odd, even ...

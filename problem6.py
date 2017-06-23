import math

# Sum square difference
# Problem 6 
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += math.pow(i, 2)
    return sum

def square_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return math.pow(sum, 2)

print(sum_squares(3))
print(square_sum(100) - sum_squares(100))

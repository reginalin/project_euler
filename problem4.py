# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

#recursive helper function for check_palindrome
def is_palindrome(first, last, num):
    num_list = [int(d) for d in str(num)]
    if (first == last or first > last):
        return True
    if (num_list[first] == num_list[last]):
        first += 1
        last -= 1
        return is_palindrome(first, last, num)
    return False

f = open('out.txt', 'w')

#returns True if number is palindrome
def check_palindrome(a, b, num):
    f.write("checking {0} {1} {2}\n".format(a,b, num))
    first = 0
    last = len(str(num))-1
    return is_palindrome(first, last, num)

def find_largest_palindrome():
    largest = 0
    num1 = 999
    while (num1 > 99):
        num2 = num1
        while (num2 > 99):
            maybe = num1 * num2
            if check_palindrome(num1, num2, maybe) and maybe > largest:
                largest = maybe
                break
            else:
                num2 -= 1
        num1 -= 1
    return largest

print(find_largest_palindrome())

#alt: find palindrome by reversing number and checking if equal

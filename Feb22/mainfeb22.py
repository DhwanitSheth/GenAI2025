### Project Euler Problem 2 Solution ###
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Function to find the sum of even Fibonacci numbers

def even_fibonacci_sum(limit):
    a = 1
    b = 2
    sum = 0
    limit = 50
    while b < limit:
        if b % 2 == 0:
            sum += b
        a, b = b, a+b
    return sum
result = even_fibonacci_sum(50)
print(result)
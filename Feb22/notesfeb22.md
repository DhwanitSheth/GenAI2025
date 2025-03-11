Assignment
# Assigning memory location to a variable
a = 5

Arthimetic
    +
    -
    *
    // (integer division quotient)
    % (modulus remainder)
    / (division)

Equality
    == (equals)
    != (not equals)

Logical
    and
    or
    not

Comparision
    <
    <=
    >
    >=




Project Euler Problem #1

Memory locations
    result = 0
    limit = 10
    index = 1
    until index < limit do the following
        if (index % 3 == 0) or (index % 5 == 0) then
            result = index + result
        end
        index = index + 1
    end

Steps (Algorithm)
    result = 0
    limit = 10



Project Euler Problem #6

### Project Euler Problem 6 Solution ###
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum = 0 
square_sum = 0
result = 0
limit = 10
index = 1
until index <= limit do the following
    sum = sum + index
    square_sum = square_sum + (index * index)
    index = index + 1
end
sum_square = sum * sum
result = sum_square - square_sum
print sum_square


Project Euler Problem #2

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

Project Euler Problem #3
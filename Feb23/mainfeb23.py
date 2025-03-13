# Factorial Practice

def fact(number):
    """"
    This function calculates the factorial of a number
    """
    if number == 0:
        return 1
    else:
        return number * fact(number - 1)
    
print(fact(100))



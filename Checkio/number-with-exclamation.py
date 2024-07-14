# This function should take a non-negative integer as an input and return the factorial of that number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n .

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
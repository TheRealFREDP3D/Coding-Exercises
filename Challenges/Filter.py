#! /usr/bin/python3

# 1. list all prime number between 1337 and 148608
# 2. Add all these numbers
# 3. Substract 966923583 to get the flag.
# flag format: '<integer>'

# ------------------------------------------------------------------------------------------------

# 1

range_min = 1337
range_max = 148608

def is_prime(num):
    """
    Check if the given number is a prime number.

    Parameters:
    num (int): The number to be checked for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
      
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in range(range_min, range_max) if is_prime(num)]

print(f"All prime numbers between {range_min} and {range_max} are:\n")
print(prime_numbers)
print("------------------------------------------\n")

# 2
total_sum = sum(prime_numbers)
print("Sum of all prime numbers:\n")
print(total_sum)
print("------------------------------------------\n")

# 3
flag = total_sum - 966923583
print("Flag:\n")
print(flag)
print("------------------------------------------\n")
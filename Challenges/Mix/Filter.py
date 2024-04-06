# ------------------------------------------------------------------------------------------------
# filter.py
# Made by: Frederick Pellerin
# Twitter: @TheRealFredP3D
# ------------------------------------------------------------------------------------------------
# Challenge
# 1. list all prime number between 1337 and 148608
# 2. Add all these numbers
# 3. Substract 966923583 to get the flag.
# Flag format: '<integer>'
# ------------------------------------------------------------------------------------------------

range_min = 1337
range_max = 148608
prime_numbers = []
total_sum = 0
numbers_count = 0
flag = 0

# This code snippet defines a function is_prime that checks if
# a given number is a prime number. 
# It returns True if the number is prime, and False otherwise.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# If a number is prime, add it's value to the total_sum variable.
for num in range(range_min, range_max):
    if is_prime(num):
        prime_numbers.append(num)
        total_sum += num
        
        print(f"Prime number between {range_min} and {range_max} found: {num}")
        print(f"Total is now:                            {total_sum}")
        print(f"****************************************************")        

print("\n\n\n\n\n\n\n\n\n\n-------------------------------------")
print(f"Sum of all prime numbers: {total_sum} - 966923583 =")
print("-------------------------------------")

flag = total_sum - 966923583

print(f"Flag: {flag}")
print("------------------------------------------\n")
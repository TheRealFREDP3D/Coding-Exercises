"""
# 21-Fizz-Buzz.py

Prints the numbers from 1 to 99, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", 
and multiples of both 3 and 5 with "FizzBuzz".
"""
for i in range(1, 100, 1):
    if (i % 3 == 0) and (i % 5 == 0) == True:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(f"{i}")

# fizz-buzz.py

# "Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

# You should write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;
# The number as a string for other cases.



# Taken from mission Just Fizz!

def checkio(num: int) -> str:
    # your code her
    if num % 3 == 0 and num % 5 ==0:
        return 'Fizz Buzz'    
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return str(num)

for i in range(0, 101):
    print(checkio(i))

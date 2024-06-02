# The Cyclone
# Ask the height of and how many credit yo the user

print(
    'The Cyclone requirements\n\nHeight: 137 cm\nCredits: 10\n\n****************************\n'
)

user_height = int(input('What's your height: '))
user_credits = int(input('How many credits you have? : '))

if user_height >= 137 and user_credits >= 10:
    print('Enjoy the ride!')
elif user_height < 137 and user_credits > 10:
    print('You are not tall enough to ride.')
elif user_height >= 137 and user_credits < 10:
    print('You don't have enough credits')
else:
    print('You do not met the requirements')

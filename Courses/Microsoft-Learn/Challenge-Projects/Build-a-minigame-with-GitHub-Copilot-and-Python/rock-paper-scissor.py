import random


def main():
    '''
    The main function to start the game.
    '''
    while True:
        play_game()
        if input('Play again? (y/n): ').lower() == 'n':
            break


def play_game():
    '''
    The function to play one round of the game.
    '''
    # Define the possible choices
    choices = ['Rock', 'Paper', 'Scissors']

    # Get the player's choice
    player_choice = input(
        'Choose your weapon (Rock, Paper, or Scissors): '
    ).capitalize()

    # Choose a random choice for the computer
    computer_choice = random.choice(choices)
    print('Computer's choice: ' + computer_choice)
    # Compare the choices and determine the winner
    if player_choice == computer_choice:
        print('It's a tie!')
    elif (
        (player_choice == 'Rock' and computer_choice == 'Scissors')
        or (player_choice == 'Paper' and computer_choice == 'Rock')
        or (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):

        print('You win!')

    else:
        print('You lose!')


# Start the game
if __name__ == '__main__':
    main()

import random

print("This is a game of rock, paper & scissors. First to two wins! ")
game_options = ['Rock', 'Paper', 'Scissors']

user_wins = 0
computer_wins = 0

while computer_wins != 2 and user_wins != 2:
    user_choice = input('Your choice: ').capitalize()
    computer_choice = random.choice(game_options)
    print(f"Computer's choice: {computer_choice}")
    print()

    if user_choice == 'Rock' or user_choice == 'Paper' or user_choice == 'Scissors':
        if user_choice == 'Rock':
            if computer_choice == 'Paper':
                computer_wins += 1
            elif computer_choice == 'Scissors':
                user_wins += 1
            else:
                pass
        if user_choice == 'Paper':
            if computer_choice == 'Scissors':
                computer_wins += 1
            elif computer_choice == 'Rock':
                user_wins += 1
            else:
                pass
        if user_choice == 'Scissors':
            if computer_choice == 'Paper':
                user_wins += 1
            elif computer_choice == 'Rock':
                computer_wins += 1
            else:
                pass


if computer_wins > user_wins:
    print('Computer wins!')
else:
    print('You win!')

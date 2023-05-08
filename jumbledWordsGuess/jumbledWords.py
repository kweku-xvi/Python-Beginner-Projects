import random

print("""
This is a word guessing game where you try to guess the correct word of the jumbled word given to you! You have three(3) guesses
""")

words_jumbled = ['almsina', 'esexirce', 'nyeger', 'udrag', 'hnytpo']
words_correct = ['animals', 'exercise', 'energy', 'guard', 'python']

def word_guess():
    n = len(words_jumbled)
    guesses = 1

    num = random.randint(0, n - 1)

    print(f'Jumbled word: {words_jumbled[num]}')

    while guesses <= 3:
        guess = input("Enter guess: ").lower()

        if guess == words_correct[num]:
            print("You win!")
            break
        elif guess != words_correct[num] and guesses < 3:
            print("Try Again!")
        guesses += 1
    else:
        print("You lose!")


option = input("Do you want to play the game? (Yes/No) ").capitalize()

while True:
    if option == 'Yes':
        word_guess()
    else:
        exit()

    print()
    option = input("Play Again? (Yes/No) ").capitalize()
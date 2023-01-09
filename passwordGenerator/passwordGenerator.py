import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    passwordLength = int(input('How many characters are in the password? '))

    random.shuffle(characters)

    password = []

    for x in range(passwordLength):
        password.append(random.choice(characters))

    random.shuffle(characters)

    password = "".join(password)

    print(password)



option = input('Do you want to generate a password? (Yes/No) ').capitalize()

if option == 'Yes':
    generate_password()
else:
    exit()




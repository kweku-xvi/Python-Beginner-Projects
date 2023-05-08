import string
import random

characters = list(string.digits)

def pin_generator():
    pinLength = int(input("How many characters are in the pin? "))

    random.shuffle(characters)

    pin = []

    for x in range(pinLength):
        pin.append(random.choice(characters))

    random.shuffle(characters)

    pin = "".join(pin)

    print(pin)


while True:
    option = input("Do you want to generate a pin? (Yes/No) ").capitalize()

    if option == "Yes":
        pin_generator()
    else:
        exit()
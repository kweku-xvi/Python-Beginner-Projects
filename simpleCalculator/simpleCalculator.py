def add(a, b):
    answer = a + b
    print(f'{a} + {b} = {answer}')


def sub(a, b):
    answer = a - b
    print(f'{a} - {b} = {answer}')

def mul(a, b):
    answer = a * b
    print(f'{a} * {b} = {answer}')


def div(a, b):
    answer = a / b
    print(f'{a} / {b} = {answer}')


while True:
    print(f'''
A - Addition
B - Substraction
C- Multiplication
D - Division
E - Exit
    ''')
    choice = input('Enter your choice: ').upper()
    if choice == "A":
        print('Addition')
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the other number: '))
        add(first_number, second_number)
    elif choice == "B":
        print('Substraction')
        first_number = float(input('Enter the first number number: '))
        second_number = float(input('Enter the other number: '))
        sub(first_number, second_number)
    elif choice == "C":
        print('Multiplication')
        first_number = float(input('Enter the first number number: '))
        second_number = float(input('Enter the other number: '))
        mul(first_number, second_number)
    elif choice == "D":
        print('Division')
        first_number = float(input('Enter the first number number: '))
        second_number = float(input('Enter the other number: '))
        div(first_number, second_number)
    elif choice == 'E':
        print('Program ended!')
        exit()

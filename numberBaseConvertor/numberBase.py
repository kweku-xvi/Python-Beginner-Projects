def from_base_10(number, newBase):
    remainders = []
    remainder = 1

    while number > 0:
        if number == 1:
            remainders.append(1)
        else:
            remainder = number % newBase
            remainders.append(remainder)
        number //= newBase

    remainders.reverse()

    for i in remainders:
        if i == 10:
            print("A", end = "")
        elif i == 11:
            print("B", end = "")
        elif i == 12:
            print("C", end = "")
        elif i == 13:
            print("D", end = "")
        elif i == 14:
            print("E", end = "")
        elif i == 15:
            print("F", end = "")
        else:
            print(i, end = "")


def to_base_10(number, base):
    power = len(number) - 1
    answer = 0

    for i in range(len(number)):
        if number[i] == "A":
            answer += 10 * base ** power
        elif number[i] == "B":
            answer += 11 * base ** power
        elif number[i] == "C":
            answer += 12 * base ** power
        elif number[i] == "D":
            answer += 13 * base ** power
        elif number[i] == "E":
            answer += 14 * base ** power
        elif number[i] == "F":
            answer += 15 * base ** power
        else:
            answer += int(number[i]) * base ** power
        power -= 1
    print(answer)


base = int(input("Enter the current base of the number: "))

if base == 10:
    number = int(input("Enter the number: "))
    newBase = int(input("Enter the base to be converted to: "))
    from_base_10(number, newBase)
elif base != 10:
    number1 = input("Enter the number: ").upper()
    newBase = int(input("Enter the base to be converted to: "))
    if newBase == 10:
        to_base_10(number1, base)
    
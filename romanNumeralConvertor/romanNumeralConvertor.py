print()
print("Roman Numeral generator for the first 1000 integers")
print()

class RomanNumeralConvertor:
    def __init__(self, num):
        self.num = num

    def firstFive(self): # generating the roman numerals for the first five numbers
        count = 0
        roman_numeral = ""
        temp = self.num

        if self.num < 4:
            while self.num > 0:
                roman_numeral += "I"
                self.num -= 1
        elif self.num == 4:
            roman_numeral = "IV"
        else:
            roman_numeral = "V"
        print(f'The Roman Numeral for {temp} is {roman_numeral}')

    def sixToTen(self): # generating the roman numerals for numbers from 6 to 10
        temp = self.num

        if self.num < 9:
            roman_numeral = "V"
            while self.num > 5:
                roman_numeral += "I"
                self.num -= 1
        elif self.num == 9:
            roman_numeral = "IX"
        else:
            roman_numeral = "X"
        print(f'The Roman Numeral for {temp} is {roman_numeral}')

    def otherNumbers(self): # generating roman numerals for numbers from 10 to 1000
        # temporary storage units for the number
        temp = self.num
        zero_count = 0 # to count the number of zeros if number is greater than 100
        roman_numeral = ""

        numerals_in_hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"]
        numerals_in_tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C"]
        numerals_one_to_ten = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

        # finding the roman numeral for the hundred the number is in
        if self.num > 100 and self.num <= 1000:
            while self.num >= 100:
                self.num = self.num - 100
                zero_count += 1
            roman_numeral += numerals_in_hundreds[zero_count - 1]
        else:
            pass

        if self.num == 0:
            pass
        elif not self.num == 0 and self.num <= 10: # if the remaining number after getting the roman numeral for the hundred the number is in is less than 10 
            roman_numeral += numerals_one_to_ten[self.num - 1]
        else: # if the remaining number after getting the roman numeral for the hundred the number is in is > 10
            copy_num = self.num // 10
            roman_numeral += numerals_in_tens[copy_num - 1]
            last_number = self.num % 10
            if not last_number == 0:
                roman_numeral += numerals_one_to_ten[last_number - 1]
            else:
                pass

        print(f'The Roman Numeral for {temp} is {roman_numeral}')


while True:
    condition = input("Do you want to generate the Roman Numeral of a number?(Y/N): ").lower()

    if condition == 'y':
        number = int(input("Enter the number: "))
        roman = RomanNumeralConvertor(number)

        if number > 0 and number <= 5:
            roman.firstFive()
            print()
        elif number > 5 and number <= 10:
            roman.sixToTen()
            print()
        else:
            roman.otherNumbers()
            print()
    else:
        print("Thanks for using this roman numeral convertor!")
        exit()

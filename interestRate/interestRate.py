def main():
    print('This is a monthly payment loan calculator: ')
    print()


main()
principal = float(input('Input the loan amount: '))
apr = float(input('Input the annual interest rate: '))
years = int(input('Input amount of years: '))

monthlyInterestRate = apr / 1200
months = years * 12
monthlyPayment = principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-months))

print('The monthly payment of the loan is %.2f ' % monthlyPayment)
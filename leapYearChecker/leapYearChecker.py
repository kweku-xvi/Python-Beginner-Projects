def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year')
            else:
                print('Not Leap Year')
        else:
            print('Leap Year')
    else:
        print('Not Leap Year')


year_input = int(input('Input Year: '))
is_leap_year(year_input)
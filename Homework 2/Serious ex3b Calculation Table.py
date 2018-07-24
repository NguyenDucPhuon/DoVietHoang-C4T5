n = 9
column = 0
while column < n:
    print('')
    column += 1
    for line in range(1, n + 1):
        semester = column * line
        numbers_of_digit = int(len(str(semester)))

        print( semester, end = '' )
        numbers_of_space = 7 - numbers_of_digit
        print(numbers_of_space * " ", end ='')

print('')
number = int(input("Enter a number: "))
column = 0
while column < number:
    print('')
    column += 1
    for line in range(1, number + 1):
        semester = column * line
        numbers_of_digit = int(len(str(semester)))

        print( semester, end = '' )
        numbers_of_space = 7 - numbers_of_digit
        print(numbers_of_space * " ", end ='')

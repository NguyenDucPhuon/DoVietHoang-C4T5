number = 20
for i in range (number + 1):
    if i % 2 == 0:
        print(1, end = '  ')
    else:
        print(0, end = '  ')

print('')
number = int(input("Enter the total number of 1's and 0's: "))
for i in range (number + 1):
    if i % 2 == 0:
        print(1, end = '  ')
    else:
        print(0, end = '  ')
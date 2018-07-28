import random

with open("dictionary.txt") as file:
    words = file.read().splitlines()
    length = int(len(words))
    index = random.randint(1, length)
    level = int(input("""
We have 3 levels (1, 2, 3)
What levels do you want to begin with? """))

    while int(len(words[index])) != (level + 2*level) :
        index += 1
    # print(words[index])
    # x = [ [i] for i in range (len(words[index]))]
    # random.shuffle(x)
    # print(x)

    a = range(len(words[index]))
    b = random.sample(a, len(a)) #shuffle
    for i in range (len(b)):
        print(words[index][b[i]], end = '  ')

    print('')
    your_guess = input("Your guess: ")
    if your_guess == words[index]:
        print("You are lucky!")
    else:
        print("Bobo cyka blyat, noob baka. Delete dota plss.")
        print(f"The answer is: {words[index]}")

#game kho vlon anh oi
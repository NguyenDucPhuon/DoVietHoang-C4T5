from random import randint

print("Hello, my name is Hoang and these are my ship sizes: ")
ship_sizes = [ '', '', '', '', '', '', '']
length = int(len(ship_sizes))
for i in range(length):
    ship_sizes[i] = randint(1,300)
print(ship_sizes)



months = int(input("How many months I have raised my ship? "))
start = 0
while start < months:
    start += 1
    for i in range (length):
        ship_sizes[i] += 50
    print("""
    
    """)
    print(f"Month {start}: ")
    print("One month has pass, now here is my flock: ")
    print(ship_sizes)
    max_size = max(ship_sizes)
    index = 1
    for i in range(length):
        if max_size == ship_sizes[i]:
            index = int(i)

    print(f"Now my biggest ship has size {max_size} let's shear it. ")
    ship_sizes[index] = 8

    print("After shearing, here is my flock")
    print(ship_sizes)

print("""

""")
total = sum(ship_sizes)
print(f"My flock has size in total: {total}")
money = total * 2
print(f"I would get {total} * 2$ = {money}$")
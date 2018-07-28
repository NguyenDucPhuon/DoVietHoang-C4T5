from turtle import *
speed(0)
n = 3
colors = [ "red", "blue", "brown", "yellow", "gray"]
while n < 8:

    for i in range (n):
        color(colors[n - 3])
        forward(100)
        left(180 - 180 * (n - 2) / n)
    n = n + 1
mainloop()
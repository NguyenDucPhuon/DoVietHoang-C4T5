from turtle import *
speed(0)

colors = [ "red", "blue", "brown", "yellow", "gray"]
index = 0
for index in range (5):
    color(colors[index], colors[index])
    begin_fill()

    for i in range(2):
        forward(50)
        left(90)
        forward(80)
        left(90)

    forward(50)
    end_fill()
index += 1
mainloop()
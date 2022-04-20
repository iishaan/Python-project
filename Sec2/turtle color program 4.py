import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
sides = eval (input("please enter a side of 2 to 10 sides: "))
colors = ['red','blue','green','yellow','orange','purple','gray','white','pink','light blue']
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 100)
import turtle
t = turtle.Pen()
t.speed(00)
turtle.bgcolor("black")
sides = 10
colors = ["red","blue","green","yellow","orange","purple","gray","white","pink","light blue"]
for x in range(1000):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 100)        
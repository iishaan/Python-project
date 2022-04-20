import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
your_name = turtle.textinput("enter a name","What is your name")
colors = ["red","blue","green","yellow","orange","purple","gray","white","pink","light blue"]
for x in range(10000):
    t.pencolor(colors[x % 4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(your_name,font = ("Times",int((x + 4)/4),"bold"))
    t.left(91)      
    t.hideturtle()

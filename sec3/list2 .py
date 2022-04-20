import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
circle = int (turtle.numinput("Number of circle","please enter a circle of 1 to 10 circle: "))
colors = ['red','blue','green','yellow','orange','purple','gray','white','pink','light blue']
for x in range(500):
    t.pencolor(colors[x % circle])
    t.circle(x)
    t.left(360 / circle + 1)
    t.width(x * circle / 100)    
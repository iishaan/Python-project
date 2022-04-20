
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
sides = int(turtle.numinput("Number of sides",
            "How many sides in your spiral?", 4))
colors = ['red','blue','green','yellow','orange','purple','gray','white','pink','light blue']           
for m in range(5,75):   
    t.left(360/sides + 5)
    t.width(m//25+1)
    t.penup()        
    t.forward(m*4)   
    t.pendown()     
    if (m % 2 == 0):
        for n in range(sides):
            t.pencolor(colors [n %sides])
            t.circle(m/3)
            t.right(360/sides)
            t.hideturtle()
    else:
        for n in range(3,m):
            t.forward(m)
            t.right(360/sides)
            t.hideturtle()


   



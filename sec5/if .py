answer = input("do you want to see a speiral? yes/no: ")
if answer =='yes':
    print("Working.......")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(100): 
        t.forward(2*x)
        t.left(89)
print("Okey,we are done")
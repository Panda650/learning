import turtle
tu = turtle.Turtle()
tu.screen.bgcolor("white") #background color
tu.pensize(2) #size of pen
tu.color("maroon") # the log tree color
tu.left(90)
tu.backward(100)
tu.speed(200)
tu.shape('turtle') #shape of pen

def tree(i):
    if i < 10:
        return
    else:
        tu.forward(i)
        tu.color("silver")  #fruits color
        tu.circle(2)
        tu.color("brown")  #twigs color
        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)

tree(100) #tree size
turtle.done()
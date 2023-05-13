#------------- Initializing Turtle and Screen Colour ---------------

import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("black")


t.penup()
t.goto(-230,175)
t.pendown()

#--------------- I letter Drawing Code ------------------

t.pencolor("white")
t.pensize(15)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(170)
t.right(90)
t.forward(50)
t.backward(100)

t.penup()
t.goto(0,0)
t.pendown()

#------------ Heart Shape Drwaing Code --------------

t.color("red")
t.begin_fill()
t.right(130)
t.forward(133)
t.circle(50,200)
t.right(140)
t.circle(50,200)
t.forward(133)
t.end_fill()

t.penup()
t.goto(140,175)
t.pendown()

#--------------- U Letter Drwawing Code --------------

t.pencolor("white")
t.right(40)
t.forward(120)
t.circle(60,180)
t.forward(120)

t.penup()
t.goto(-75,-150)
t.pendown()
t.write("Yash", font=("Arial",50,"bold"))

t.hideturtle()
turtle.done()
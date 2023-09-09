import turtle
from random import *

screen = turtle.Screen()
screen.bgcolor("white")
canvas = screen.getcanvas()
turtle.shape("turtle")
turtle.colormode(255)

def square() :
    size = randint(50,200)
    i = 0
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.penup()
    turtle.pencolor(r,g,b)
    turtle.setposition(randint(-700,700), randint(-250,400))
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()
    turtle.pendown()
    while i < 4 :
        i = i + 1
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def triangle() :
    size = randint(50,200)
    i = 0
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.penup()
    turtle.pencolor(r,g,b)
    turtle.setposition(randint(-700,700), randint(-250,400))
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()
    turtle.pendown()
    for x in range(3) :
        turtle.forward(size)
        turtle.right(120)
    turtle.end_fill()

def circle() :
    size = randint(50,200)
    i = 0
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.penup()
    turtle.pencolor(r,g,b)
    turtle.setposition(randint(-700,700), randint(-400,300))
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(int(size / 2))
    turtle.end_fill()

i = 0
while i < 15 :
    i = i + 1
    shape_select = randint(1,3)
    if shape_select == 1 :
        circle()
    elif shape_select == 2 :
        square()
    else :
        triangle()

screen.exitonclick()
turtle.done() 

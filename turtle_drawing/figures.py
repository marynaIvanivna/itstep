# import turtle
# turtle.shape("turtle")

from turtle import *
shape("turtle")
pensize(10)

pencolor("green") # прямокутник
forward(150)
left(90)
forward(100)
left(90)
forward(150)
left(90)
forward(100)
left(90)

pencolor("blue") # коло
circle(50)

left(90)  # перехід
penup()
forward(100)
pendown()

pencolor("red") # трикутник
right(30)
forward(150)
right(120)
forward(150)
right(120)
forward(150)

exitonclick()
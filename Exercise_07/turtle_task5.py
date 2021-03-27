import turtle
import random

t = turtle.Pen()
turtle.bgcolor("black")
colors= ["red", "yellow", "blue", "green"]

name = turtle.textinput("Enter your name:", "What is your name")

for x in range(100):
    index=random.randint(0,3)
    t.pencolor(colors[index])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(name, font= ("Arial", int((x+4)/4), "bold"))
    t.left(92)


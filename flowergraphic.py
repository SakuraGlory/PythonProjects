import turtle
from turtle import *
t = turtle.Turtle()

def fleur() :
    for i in range(300):
        t.fillcolor("blue")
        t.begin_fill()
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)

fleur()
mainloop()
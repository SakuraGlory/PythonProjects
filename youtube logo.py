import turtle
t=turtle.Turtle()
s=turtle.Screen()
t.hideturtle()
t.fillcolor("#c4302b")

t.begin_fill()
for j in[300,200,]*2:
    t.forward(j)
    t.circle(50,90)
t.end_fill()
t.penup()
t.goto(120,100)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for j in [30,120,120]:
     t.left(j)
     t.forward(100)
t.end_fill()
turtle.done()






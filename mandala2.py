import turtle
import random
t = turtle.Turtle()
t.screen.bgcolor("black")
turtle.title("Mandala na matiku")
t.color("green")
t.speed(0)
def pen(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def pattern():
    for i in range(23):
        t.forward(360)
        t.circle(20)
        t.left(216+3)

pen(-200,100)
pattern()
t.color("red")
pen(-30,-184)
t.circle(220)
pen(-30,-194)
t.circle(230)
pen(-30,-144)
t.circle(180)
pen(-21,-10)
t.circle(46)

t.hideturtle()
turtle.exitonclick()

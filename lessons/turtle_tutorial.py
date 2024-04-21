"""Turtle tutorial."""

__author__ = "730664108"


from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255)
leo.color(150, 150, 150)

leo.penup()
leo.goto(-120, -120)
leo.pendown()
leo.hideturtle()
leo.speed(50)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color("black")

bob.penup
bob.goto(-120, -120)
bob.pendown
bob.speed(60)
side_length: int = 300
while i < 100:
    bob.forward(side_length)
    bob.left(122)
    side_length = side_length * .97
    i = i + 1

done()
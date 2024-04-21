"""Turtle drawing thing of a mountain scene."""

__author__ = "730664108"

from turtle import Turtle, colormode, done

brush: Turtle = Turtle()
brush.speed(100)


def main() -> None:
    """The entrypoint of my scene."""
    brush: Turtle = Turtle()
    brush.speed(100)
    done()


def draw_2_mountains(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws the two main mountains for the scene."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    colormode(255)
    a_turtle.color(155, 155, 155)
    a_turtle.begin_fill()
    
    def draw_mountain(steps: int) -> None:
        """Recusrsive functon to make mountain outlines an fill first mountain."""
        if steps > 0:
            a_turtle.forward(400)
            a_turtle.left(120)
            draw_mountain(steps - 1)
    draw_mountain(3)
    a_turtle.goto(x + 400, y)
    a_turtle.pendown()
    draw_mountain(6)
    i: int = 0
    while (i < 3):
        a_turtle.forward(400)
        a_turtle.left(120)
        i += 1
    a_turtle.end_fill()


def grass(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws the grass base."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown
    a_turtle.color("darkgreen", "chartreuse3")
    a_turtle.begin_fill()
    i: int = 0
    while (i < 2):
        a_turtle.forward(800)
        a_turtle.right(90)
        a_turtle.forward(400)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def tree(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws a tree at a certain coordinate."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("chocolate4")
    a_turtle.begin_fill()
    i: int = 0
    while (i < 2):
        a_turtle.forward(25)
        a_turtle.left(90)
        a_turtle.forward(50)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()
    a_turtle.penup()
    a_turtle.left(90)
    a_turtle.forward(40)
    a_turtle.right(90)
    a_turtle.forward(12.5)
    a_turtle.color("green")
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(25)
    a_turtle.end_fill()


def birds(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws a group of birds at a certain coordinate."""
    a_turtle.color("black")
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.left(30)
    a_turtle.forward(30)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.left(90)
    a_turtle.forward(30)
    # Second bird.
    a_turtle.penup()
    a_turtle.goto(x - 30, y - 30)
    a_turtle.right(90)
    a_turtle.pendown()
    a_turtle.left(30)
    a_turtle.forward(30)
    a_turtle.penup()
    a_turtle.goto(x - 30, y - 30)
    a_turtle.pendown()
    a_turtle.left(90)
    a_turtle.forward(30)
    # Third bird.
    a_turtle.penup()
    a_turtle.goto(x + 30, y - 30)
    a_turtle.right(145)
    a_turtle.pendown()
    a_turtle.left(30)
    a_turtle.forward(30)
    a_turtle.penup()
    a_turtle.goto(x + 30, y - 30)
    a_turtle.pendown()
    a_turtle.left(90)
    a_turtle.forward(30)
    # Fourth bird.
    a_turtle.penup()
    a_turtle.goto(x + 60, y)
    a_turtle.right(110)
    a_turtle.pendown()
    a_turtle.left(30)
    a_turtle.forward(30)
    a_turtle.penup()
    a_turtle.goto(x + 60, y)
    a_turtle.pendown()
    a_turtle.left(90)
    a_turtle.forward(30)


def sun(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws the sun."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("orange", "yellow")
    a_turtle.begin_fill()
    a_turtle.circle(125)
    a_turtle.end_fill()


sun(brush, 100.0, 100.0)
draw_2_mountains(brush, -400.0, -100.0)
grass(brush, -400.0, -100.0)
tree(brush, -200.0, -200)
tree(brush, 300.0, -250.0)
tree(brush, -75.0, -300.0)
birds(brush, 0.0, 300.0)

if __name__ == "__main__":
    main()
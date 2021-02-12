from itertools import permutations
from random import choice
from turtle import *

screen = Screen()
screen.screensize(1366, 768)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.bgcolor("white")


def star_multiple(turtle):
    colors = [
        "red",
        "orange",
        "blue",
        "green",
        "cyan",
        "chocolate",
        "pink",
        "yellow",
        "lavender",
    ]
    combos = list(permutations(colors, 2))
    clist = [choice(combos), choice(combos)]
    for i in range(40, 120, 10):
        if (i / 10) % 2 == 0:
            drawstar(turtle, 150 - i, clist[0])
        else:
            drawstar(turtle, 150 - i, clist[1])


def pen(foo):
    lst = [a, b, c, d]
    for i in lst:
        i.__getattribute__(foo)()


def drawstar(turtle, l, colors):
    global screen
    turtle.ht()
    turtle.color(*colors)
    turtle.begin_fill()
    i = 0
    while i < 5:
        turtle.left(15)
        turtle.forward(l)
        turtle.left(130)
        turtle.forward(l)
        i += 1
    turtle.end_fill()


a, b, c, d = Turtle(), Turtle(), Turtle(), Turtle()
pen("penup")
a.speed(10), b.speed(10), c.speed(10), d.speed(10)
a.goto(-500, 180), b.goto(500, 180), c.goto(-500, -250), d.goto(500, -250)
pen("pendown")
for i in [a, b, c, d]:
    star_multiple(i)
penup()
goto(-300, 250)


def H():
    pendown()
    color("white", "red")
    begin_fill()
    seth(270), forward(100), left(90), forward(30)
    left(90), forward(40), right(90), forward(60), right(90), forward(40)
    left(90), forward(30), left(90), forward(
        100), left(90), forward(30), left(90)
    forward(40), right(90), forward(60), right(90), forward(40), left(90), forward(
        30
    ), end_fill()


def A():
    seth(0), forward(30), pendown()
    begin_fill()
    seth(300), forward(116), seth(180), forward(30), seth(120), forward(40), seth(
        180
    ), forward(20)
    seth(240), forward(40), seth(180), forward(30), seth(60), forward(116)
    end_fill()


def P():
    begin_fill(), pendown(), seth(270), forward(100), seth(0), forward(25)
    seth(90), fd(50), seth(0), circle(26, 180), fd(25)
    end_fill()


def Y():
    pendown(), begin_fill()
    seth(300), fd(60), seth(270), fd(50), seth(0), fd(25), seth(90), fd(50)
    seth(60), fd(60), seth(180), fd(22), seth(240), fd(40), seth(120), fd(40)
    seth(180), fd(22), end_fill()


def N():
    pendown(), begin_fill()
    seth(270), fd(100), seth(0), fd(30), seth(90), fd(70), seth(300), fd(80)
    seth(0), fd(30), seth(90), fd(100), print(pos()), seth(180), fd(30), seth(270), fd(
        70
    )
    seth(120), fd(85), seth(180), fd(30), end_fill()


def E():
    pendown(), begin_fill(), seth(0), fd(100), seth(270), fd(20), seth(180), fd(70)
    seth(270), fd(20), seth(0), fd(60), seth(270), fd(20), seth(180), fd(60)
    seth(270), fd(20), seth(0), fd(70), seth(270)
    fd(20), seth(180), fd(100), seth(90), fd(100), end_fill()


def W():
    pendown(), begin_fill()
    seth(0), fd(30), seth(300), fd(80), seth(60), fd(60), seth(300), fd(60), seth(
        60
    ), fd(80), seth(0), fd(30)
    seth(240), fd(100), seth(180), fd(30), seth(120), fd(40), seth(240), fd(40), seth(
        180
    ), fd(30), seth(120), fd(100)
    end_fill()


def R():
    pendown(), begin_fill()
    seth(270), fd(100), seth(0), fd(30), seth(90), fd(40), seth(300), fd(50), seth(
        30
    ), fd(30), seth(120), fd(50)
    seth(0), circle(25, 180), fd(60), end_fill()


speed(10)
H(), penup(), backward(170)
A(), penup(), seth(0), forward(80)
P(), penup(), seth(0), fd(70)
P(), penup(), seth(0), fd(70)
Y(), penup(), goto(-250, 80)
N(), penup(), seth(0), fd(120)
E(), penup(), seth(0), fd(120)
W(), penup(), goto(-270, -90)
Y(), penup(), seth(0), fd(100)
E(), penup(), seth(0), fd(140)
A(), penup(), seth(0), fd(70)
R(), ht(), done()

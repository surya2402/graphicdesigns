import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Bhai ki programming")

h = turtle.Turtle()
h.pencolor("white")
h.speed(0)
h.width(6)
h.pencolor("orange")
h.hideturtle()


def curve():
    for i in range(60):
        h.left(3)
        h.forward(1)


def curveyebrow():
    for i in range(30):
        h.forward(6)
        h.right(2)


def curvenose():
    for i in range(15):
        h.forward(1)
        h.right(1)


def curvenosepoint1():
    for i in range(10):
        h.forward(2)
        h.right(1)


def curvenosepoint2():
    for i in range(5):
        h.forward(2)
        h.right(1)


def belownoseline1():
    for i in range(8):
        h.forward(6)
        h.left(5)


def belownoseline2():
    for i in range(8):
        h.forward(5)
        h.right(5)


def upperlip():
    for i in range(10):
        h.forward(10)
        h.left(10)
    for x in range(10):
        h.forward(3)
        h.right(10)


def lowerlip():
    for i in range(10):
        h.forward(6)
        h.right(6)


def chincurve():
    for i in range(15):
        h.forward(12)
        h.left(6)


def eye():
    for i in range(10):
        h.forward(8)
        h.right(4)
    for a in range(10):
        h.forward(2)
        h.left(7)


# position of design
h.penup()
h.goto(-100, 250)
h.pendown()


h.right(80)
h.forward(70)
curve()
h.forward(70)
h.backward(70)
h.penup()
h.left(90)
h.width(10)
h.forward(20)
h.pendown()
h.pencolor("white")
h.right(90)
h.forward(60)
h.backward(60)
h.penup()
h.right(90)
h.forward(40)
h.pendown()
h.pencolor("red")


h.width(15)
h.left(30)
h.forward(10)
curveyebrow()


h.right(140)
h.penup()
h.forward(230)
h.width(8)
h.forward(10)
h.left(79)
h.forward(10)
h.pendown()
h.left(90)
h.width(10)
h.right(80)
h.forward(20)
h.right(25)
h.width(10)
h.forward(70)
h.left(60)
h.forward(30)
curvenose()
h.width(5)
h.left(60)


h.penup()
h.forward(20)
h.left(80)
h.forward(5)
h.pendown()
h.width(8)
h.forward(5)
h.right(45)
h.width(8)
h.forward(5)
curvenosepoint1()

h.penup()
h.forward(15)
h.pendown()
h.width(10)
h.right(120)
h.forward(15)
h.right(40)
h.forward(20)
h.right(20)
h.forward(10)
curvenosepoint2()

h.penup()
h.right(30)
h.forward(30)
h.left(100)
h.forward(15)
h.pendown()
h.width(5)
h.forward(5)
belownoseline1()

h.penup()
h.left(70)
h.forward(15)
h.left(90)
h.pendown()
h.width(5)
h.forward(10)
belownoseline2()

h.penup()
h.backward(45)
h.right(110)
h.forward(30)
h.pendown()
h.width(10)
h.forward(5)
upperlip()

h.penup()
h.right(100)
h.forward(70)
h.pendown()
h.right(30)
h.forward(15)
lowerlip()


h.penup()
h.backward(23)
h.left(150)
h.pendown()
h.forward(10)
chincurve()


h.penup()
h.left(100)
h.forward(350)
h.pendown()
h.right(90)
h.forward(15)
eye()

h.penup()
h.backward(50)
h.left(90)
h.forward(40)
h.dot(30, "red")
h.dot(10, "black")

def setPosition(x, y):
    h.penup()
    h.goto(x, y)
    h.pendown()

setPosition(-150, -220)
h.color("orange")
h.write("Glory to hanuman"
        " ",
font=("Calibri", 25, "bold")
)

turtle.done()
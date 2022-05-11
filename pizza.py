import turtle

PIZZA_COLOR = "#FBC70F"
PIZZA_CRUST_COLOR = "#ECA84F"
PIZZA_TOPPING_COLOR = "#AD0509"
BGCOLOR = "#9EC388"

PIZZA_TOPPING_LOCATIONS = [
    [-70, 105],
    [-50, 120],
    [-30, 75],
    [-10, 135],
    [30, 70],
    [45, 140],
    [50, 85],
    [0, 105],
    [55, 110],
    [-20, 155],
    [10, 105],
    [25, 175]
    ]

screen = turtle.Screen()
screen.bgcolor(BGCOLOR)
screen.title("drawing pizza in python")

pizza = turtle.Turtle()
pizza.shape("circle")
pizza.pensize(5)

def drawCircle(radius, linecolor, fillcolor):
    pizza.fillcolor(fillcolor)
    pizza.color(linecolor)
    pizza.begin_fill()
    pizza.circle(radius)
    pizza.end_fill()

def moveTurtle(x, y):
    pizza.up()
    pizza.goto(x, y)
    pizza.down()

drawCircle(120, PIZZA_CRUST_COLOR, PIZZA_CRUST_COLOR)

moveTurtle(0,20)

drawCircle(100, PIZZA_COLOR, PIZZA_COLOR)

for loc in PIZZA_TOPPING_LOCATIONS:
    moveTurtle(loc[0], loc[1])
    drawCircle(10, PIZZA_TOPPING_COLOR, PIZZA_TOPPING_COLOR)

moveTurtle(0,120)

pizza.color(BGCOLOR)
for x in range(0,8):
    pizza.forward(120)
    pizza.penup()
    pizza.backward(120)
    pizza.left(45)
    pizza.pendown()

pizza.hideturtle()
turtle.done()

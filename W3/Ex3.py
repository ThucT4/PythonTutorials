import turtle
from time import sleep


def draw_equilateral_triangle(turtle):
    turtle.down()
    turtle.showturtle()

    for i in range(3):
        turtle.forward(120)
        turtle.left(120)


def draw_square(turtle):
    turtle.down()
    turtle.showturtle()

    for i in range(4):
        turtle.forward(120)
        turtle.left(90)


def draw_hexagon(turtle):
    turtle.down()
    turtle.showturtle()

    for i in range(6):
        turtle.forward(80)
        turtle.left(60)


def draw_octagon(turtle):
    turtle.down()
    turtle.showturtle()

    for i in range(8):
        turtle.forward(60)
        turtle.left(45)


def draw_3to8_polygons(turtle):
    turtle.clear()

    turtle.up()
    turtle.left(90)
    turtle.forward(340)
    turtle.right(90)

    for i in range(3, 9):
        turtle.up()
        turtle.right(90)
        turtle.forward(50 * (i / 2))
        turtle.left(90)
        turtle.down()

        for k in range(0, i):
            turtle.forward(50)
            turtle.left(360 / i)


if __name__ == '__main__':
    window = turtle.Screen()

    test = turtle.Turtle()
    test.pensize(5)
    test.speed(8)

    space = 80

    test.up()
    test.hideturtle()
    test.forward(space)
    test.left(90)
    test.forward(space)
    test.right(90)
    draw_equilateral_triangle(test)

    test.up()
    test.hideturtle()
    test.backward(space)
    test.right(90)
    test.forward(space)
    test.right(90)
    draw_square(test)

    test.up()
    test.hideturtle()
    test.left(180)
    test.forward(space)
    test.right(90)
    draw_hexagon(test)

    test.up()
    test.hideturtle()
    test.left(180)
    test.forward(space)
    test.left(90)
    test.forward(space)
    test.right(90)
    draw_octagon(test)

    sleep(1)

    test.right(90)
    draw_3to8_polygons(test)

    window.exitonclick()

import turtle


def draw_VN_flag():
    win = turtle.Screen()
    win.bgcolor("red")

    tur = turtle.Turtle()
    tur.color("yellow")
    tur.pensize(5)
    tur.speed(8)

    tur.up()
    tur.backward(90)
    tur.down()

    tur.fillcolor("yellow")
    tur.begin_fill()

    for i in range(5):
        tur.forward(180)
        tur.right(144)

    tur.end_fill()
    tur.hideturtle()

    win.exitonclick()


if __name__ == '__main__':
    draw_VN_flag()

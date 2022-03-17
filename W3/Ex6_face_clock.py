import turtle


def draw_face_clock():
    win = turtle.Screen()
    win.bgcolor("#00FA9A")

    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")

    for i in range(12):
        tool(90 + (i / 12 * 360))

    win.exitonclick()


def tool(degree):
    tur = turtle.Turtle()
    tur.shape("turtle")
    tur.color("blue")
    tur.pensize(4)
    tur.speed(10)

    tur.left(degree)

    tur.up()
    tur.forward(150)
    tur.down()

    tur.forward(10)
    tur.up()

    tur.forward(20)


if __name__ == '__main__':
    draw_face_clock()

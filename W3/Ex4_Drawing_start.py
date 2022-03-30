import turtle


def draw_start():
    win = turtle.Screen()

    tur = turtle.Turtle()
    tur.pensize(5)
    tur.speed(8)

    for i in range(5):
        tur.forward(180)
        tur.right(144)

    win.exitonclick()


if __name__ == '__main__':
    draw_start()

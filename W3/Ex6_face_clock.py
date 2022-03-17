import turtle
from time import sleep


def draw_face_clock():
    win = turtle.Screen()
    win.bgcolor("#00FA9A")

    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    t.pensize(4)
    t.speed(10)

    angle = 30

    for i in range(12):
        t.left(angle)

        t.up()
        t.forward(150)
        t.down()

        t.forward(10)
        t.up()

        t.forward(20)
        t.stamp()
        t.backward(180)

    win.exitonclick()


if __name__ == '__main__':
    draw_face_clock()

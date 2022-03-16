import math


def cal_cir_area():
    pi = math.pi

    r = float(input("Enter the radius: "))

    circumference = "{:.4f}".format(2 * r * pi)

    area = "{:.4f}".format(pi * (r ^ 2))

    print("The circumference (P) = ", circumference)
    print("The area (S) = ", area)


if __name__ == '__main__':
    option = 1

    while option == 1:
        cal_cir_area()

        print("\nContinue?")
        option = int(input("1. Yes\t2. No\n"))
def cal_rect_area():
    w = float(input("Enter width: "))

    h = float(input("Enter height: "))

    area = "{:.4f}".format(w*h)

    print("The area of rectangle (S) = ", area)

if __name__ == '__main__':
    option = 1

    while option == 1:
        cal_rect_area()

        print("\nContinue?")
        option = int(input("1. Yes\t2. No\n"))
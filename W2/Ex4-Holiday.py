def cal_return_day():
    # Get inputs
    start = int(input("Enter starting day number: "))

    leng = int(input("Enter the length of your stay: "))

    # Calculate will return after how many weeks
    # num_week = int((leng - (7 - start)) / 7)

    # Calculate the returning day
    res = (leng - (7 - start)) % 7

    print("\t------")

    print("You will return on day ", res)
    # , end="")

    # if num_week > 0:
    #   if num_week > 1:
    #       print(". After ", num_week, " week")

    #   else:
    #       print(". After ", num_week, " weeks")


if __name__ == '__main__':
    option = 1

    while option == 1:
        cal_return_day()

        print("\t------")

        print("Continue?")
        option = int(input("1. Yes\t2. No\n"))

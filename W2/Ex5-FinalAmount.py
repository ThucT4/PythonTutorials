def cal_final_amount():
    # Get input principal amount
    p = float(input("Enter the Principal amount (initial investment): "))

    # Get input number of years
    t = int(input("Enter the Number of year that the money will be compounded for: "))

    # Assign number of times the interest in compounded per year
    n = 12

    # Assign Annual nominal interest rate (as a decimal)
    r = 0.08

    # Calculate the Final amount
    a = p * ((1 + r / n) ** (n*t))

    print("The final amount A = ", a)


if __name__ == '__main__':
    option = 1

    while option == 1:
        cal_final_amount()

        print("\t------")

        print("Continue?")
        option = int(input("1. Yes\t2. No\n"))

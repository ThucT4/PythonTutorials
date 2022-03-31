def max_collatz(num, highest):
    if num > highest:
        highest = num

    if num == 1:
        print(1)
        print(f"Max value: {highest}")
        return

    # Number is even
    elif num % 2 == 0:
        print(f"{num}, ", end="")
        max_collatz(int(num / 2), highest)

    # Number is even odd
    else:
        print(f"{num}, ", end="")
        max_collatz(3 * num + 1, highest)


if __name__ == "__main__":
    max_collatz(85, 0)

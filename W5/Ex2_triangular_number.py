def print_triangular_numbers1(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i
        print(i, "{:6d}".format(sum))


if __name__ == "__main__":
    print_triangular_numbers1(5)

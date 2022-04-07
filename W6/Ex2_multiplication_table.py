def print_multipli_table(n):
    print(' x', end='')

    for row in range(-1, n + 1):
        if row > -1:
            print("{:2d}".format(row), end='')

        for col in range(n + 1):
            print("{:6d}".format(abs(col * row)), end='')

        print()


if __name__ == '__main__':
    print_multipli_table(12)

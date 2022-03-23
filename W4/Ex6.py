def ex6(n):
    while n >= 0:
        for i in range(1, n + 1):
            print(i, " ", end='')

        n -= 1
        print()


if __name__ == '__main__':
    ex6(8)

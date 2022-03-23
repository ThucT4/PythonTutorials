def is_prime(n):
    for i in range(4, n + 1):
        check = True
        for k in range(2, i//2):
            # If it is divisible by any number
            if i % k == 0:
                check = False
                break

        if check:
            print("{0:>4}".format(i), end='')

    print()


if __name__ == '__main__':
    is_prime(100)

from Ex1_isEven import is_even


def is_odd(n):
    return not is_even(n)


if __name__ == '__main__':
    print(is_odd(8))
    print(is_odd(3))
    print(is_even(0))

def number_of_digit(num):
    if not isinstance(num, int):
        return 0

    s = str(num)
    count = 0

    for ch in s:
        count += 1

    return count


if __name__ == '__main__':
    print(number_of_digit(1234))

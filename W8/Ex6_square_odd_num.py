def square_odd_num(input_sequence):
    input_list = list(map(int, input_sequence.split(',')))

    res = map(lambda x: x ** 2, filter(lambda x : x%2 != 0, input_list))

    return list(res)


if __name__ == "__main__":
    output = square_odd_num('1, 2, 3, 4, 5, 6, 7, 8, 9')

    print(','.join(map(str, output)))

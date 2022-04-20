from W4.Ex1_isEven import is_even
from Ex4_filter_even_number import filter_even_num


def is_square(num):
    return num ** 2


def filter_square_of_even_num(input_list):
    res = map(is_square, filter(is_even, input_list))

    return list(res)


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    res_list = filter_square_of_even_num(sample)

    print(res_list)

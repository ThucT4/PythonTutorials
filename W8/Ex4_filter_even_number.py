from W4.Ex1_isEven import is_even


def filter_even_num(input):
    # res = filter_even_num()
    res = list(filter(is_even, input))

    return res


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    res_list = filter_even_num(sample)

    print(res_list)

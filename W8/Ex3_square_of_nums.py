def print_list_square_of_num():
    res = []

    for i in range(1, 21):
        res += [i**2]

    print(res)

    print(res[15:])


if __name__ == "__main__":
    print_list_square_of_num()
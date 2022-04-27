def list_square_of_num():
    res = list(map(lambda x : x**2, range(1, 101)))

    return res[-5:]


if __name__ == "__main__":
    print(list_square_of_num())

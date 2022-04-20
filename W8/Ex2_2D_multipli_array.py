# Normal way
def print_2D_array1(x, y):
    arr = []

    for num_row in range(x):
        row = []

        for num_col in range(y):
            row += [num_row * num_col]

        arr += [row]

    for i in range(len(arr)):
        print(arr[i], end='')

        if i != len(arr) - 1:
            print(',', end='')

        print()


# Nested list comprehension
def print_2D_array2(x, y):
    arr = [[X * Y for Y in range(y)] for X in range(x)]

    print(arr)


if __name__ == '__main__':
    print_2D_array1(3, 5)
    print()
    print_2D_array2(3, 5)

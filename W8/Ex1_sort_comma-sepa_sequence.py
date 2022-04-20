def print_sorted_sequence(input):
    words = input.split(",")

    # Sort the list
    words.sort()

    print(','.join(words))

    for i in range(len(words)):
        print(words[i], end='')

        if i != len(words) - 1:
            print(',', end = '')
        else:
            print()


if __name__ == "__main__":
    sample = "without,hello,bag,world"
    print_sorted_sequence(sample)

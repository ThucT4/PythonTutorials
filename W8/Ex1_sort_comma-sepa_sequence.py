def sorted_sequence(input):
    words = input.split(",")

    # Sort the list
    words.sort()

    return ','.join(words)


if __name__ == "__main__":
    sample = "without,hello,bag,world"
    print(sorted_sequence(sample))

def convert_file2dict():
    res = {}

    file = open("eng2pirate.txt")

    for line in file.readlines():
        line.strip()
        words = line.split()

        res[words[0]] = ' '.join(words[1:])

    file.close()

    return res


def trans2pirate(string, dictionary):
    res = []

    for word in string.split():
        res.append(dictionary[word])

    return ' '.join(res)


if __name__ == '__main__':
    a_str = 'yes sir hotel madam'

    dict = convert_file2dict()

    print(trans2pirate(a_str, dict))

def reverse_str(string):
    res = ''

    for idx in range(len(string)-1, -1, -1):
        res += string[idx]

    return res


if __name__ == '__main__':
    print(reverse_str("abcdrf"))
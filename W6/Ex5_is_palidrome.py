def is_palidrome(string):
    idx1 = 0

    for idx2 in range(len(string) - 1, -1, -1):

        if string[idx1] != string[idx2]:
            return False

        idx1 += 1

    return True


if __name__ == "__main__":
    print(is_palidrome("22022022"))

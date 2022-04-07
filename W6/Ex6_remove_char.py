import string


def remove_char(s, ch):
    return s.replace(ch, '')


if __name__ == "__main__":
    print(remove_char("abcdedf", 'd'))

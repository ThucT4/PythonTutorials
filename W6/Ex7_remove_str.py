def remove_str(str_input, str_remove):
    return str_input.replace(str_remove, '')


if __name__ == "__main__":
    print(remove_str("abcdedf", "df"))

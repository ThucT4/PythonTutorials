def x100_message():
    mess = str(input('Enter your message: '))

    write_to_filex100(mess)


def write_to_filex100(message):
    with open('message.txt', 'w') as file:
        file.write(message * 100)


if __name__ == '__main__':
    x100_message()

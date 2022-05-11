def add_number2lines():
    filename = str(input('Enter file you want to open: '))

    copy_content_number_lines(filename)


def copy_content_number_lines(infile_name):
    with open(infile_name, 'r') as infile:
        with open(infile_name + '(numbered).txt', 'w') as outfile:
            line_num = 1

            for line in infile.readlines():
                outfile.write('{:<4d} {}'.format(line_num, line))
                line_num += 1


if __name__ == '__main__':
    add_number2lines()

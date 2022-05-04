def write_code2file():
    fname = str(input('Enter a file name: '))

    write_file2file(fname)


def write_file2file(outfile_name):
    with open('/Users/thuc/Downloads/Study Doc/Python/Code/Tutorials/W3/draw_circle.py', 'r') as infile:
        with open(outfile_name, 'w') as outfile:
            line = infile.readlines()

            outfile.write(''.join(line))


if __name__ == '__main__':
    write_code2file()
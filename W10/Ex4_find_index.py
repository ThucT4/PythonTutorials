def check_missing_value(infile_name):
    with open(infile_name, 'r') as infile:
        line_num = 1
        num_value = 0

        for line in infile.readlines():
            if line_num == 1:
                num_value = len(line.split(','))

            if len(line.split(',')) < num_value:
                print(f'Missing value at line: {line_num}')
                
            line_num += 1


if __name__ == '__main__':
    check_missing_value('edited_vietnam.txt')

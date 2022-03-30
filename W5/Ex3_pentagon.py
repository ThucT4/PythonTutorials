def cal_num_dot(n):
    if n == 1:
        return 1

    return 5*(n-1) + cal_num_dot(n-1)


if __name__ == "__main__":
    print(cal_num_dot(4))
def is_leap_year(year):
    if year % 400 == 0:
        return True

    elif year % 4 == 0 and year % 100 != 0:
        return True

    return False


if __name__ == '__main__':
    print(is_leap_year(1992))
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2017))

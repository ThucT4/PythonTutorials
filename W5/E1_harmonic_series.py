def harmonic1(n):
    # Base case
    if n == 1:
        return 1
    else:
        return 1/n + harmonic1(n-1)


def harmonic2(n):
    res = 0

    for i in range(1, n+1):
        res += 1/i

    return res


if __name__ == "__main__":
    print(harmonic1(3))
    print(harmonic2(3))
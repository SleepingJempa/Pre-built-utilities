a = int(input())
m = int(input())


def gcd(x, y):
    if x == 0:
        return [y, 0, 1]
    else:
        t = gcd(y % x, x)
        c_x = t[2] - t[1] * (y//x)
        c_y = t[1]
        return [t[0], c_x, c_y]


print(gcd(a, m))

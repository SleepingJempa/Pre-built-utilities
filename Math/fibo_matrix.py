def fast_pow(a, b):
    ans = 1
    while b > 0:
        if b & 1 == 1:
            ans *= a
        a *= a
        b >>= 1
    return ans


def main():
    a, b = list(map(int, input().split()))
    print(fast_pow(a,b)-fast_pow(b,a))


main()

def matrix_multiply(a, b):
    row = len(a)
    col = len(b[0])
    mid = len(a[0])
    res = [x[:] for x in [[0] * col] * row]
    for i in range(row):
        for j in range(col):
            for k in range(mid):
                res[i][j] += a[i][k] * b[k][j]
    return res


def identity_matrix(n):
    res = [x[:] for x in [[0] * n] * n]
    for i in range(n):
        res[i][i] = 1
    return res


def matrix_exponentiation(a, k):
    n = len(a)
    res = identity_matrix(n)
    while k > 0:
        if k & 1 == 1:
            res = matrix_multiply(res, a)
        a = matrix_multiply(a, a)
        k >>= 1
    return res


def main():
    n = int(input())
    a = [
        [1, 1],
        [1, 0]
    ]
    f = [[1], [1]]
    ans = matrix_exponentiation(a, n)
    ans = matrix_multiply(ans, f)
    print(ans[0][0] - 1)


main()

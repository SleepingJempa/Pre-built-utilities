# input: matrix a - matrix b
def matrix_product(x, y):
    res = [x[:] for x in [[0] * len(y[0])] * len(x)]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                res[i][j] += x[i][k] * y[k][j]
    return res


def print_matrix(x):
    row = len(x)
    col = len(x[0])
    for i in range(row):
        for j in range(col):
            print(x[i][j], end=' ')
        print('')


a = [
    [2, 3],
    [5, -2]
]

b = [
    [3, 1, -2],
    [4, -1, 2]
]

print_matrix(matrix_product(a, b))
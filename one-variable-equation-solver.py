n = int(input())


def the_gcd(a, b):
    if a == 0:
        return 1 * b
    else:
        return 1 * the_gcd(b % a, a)


s = str(input())

X = [0, 0]
C = [0, 0]
side = 0

cur = +1

lst = 0

debug = False

for i in range(n):
    if debug:
        print('---')
        print(s[i])
    asc = ord(s[i]) - ord('0')
    if s[i] == '=':
        cur = 1
        lst = 0
        if debug:
            print('side changed')
        side = 1
    elif 0 <= asc <= 9:
        if debug:
            print('number')
        lst = lst * 10 + asc
        if i + 1 < n and s[i + 1] != 'x' and s[i + 1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if debug:
                print('terminated')
            if debug:
                print('C[{}] += {}'.format(side, cur * lst))
            C[side] += cur * lst
            lst = 0
        elif i == n - 1 and s[i] != 'x':
            if debug:
                print('terminated and end')
            C[side] += cur * lst
            lst = 0
        if debug:
            print('lst = {}'.format(lst))
    elif s[i] == 'x':
        if lst == 0:
            lst = 1
        if debug:
            print('reached x')
        if debug:
            print('X[{}] += {}'.format(side, cur * lst))
        X[side] += cur * lst
        if debug:
            print(cur * lst)
        lst = 0
    elif s[i] == '-':
        if debug:
            print('cur changed -')
        cur = -1
    elif s[i] == '+':
        if debug:
            print('cur changed +')
        cur = +1
    if debug:
        print('---')

if debug:
    print('leftX = {} and leftC = {}'.format(X[0], C[0]))
    print('righX = {} and righC = {}'.format(X[1], C[1]))

ofX = X[0] - X[1]
ofC = C[1] - C[0]

if debug:
    print('ofX = {}'.format(ofX))
    print('ofC = {}'.format(ofC))

sign_of_X = +1
if ofX < 0:
    sign_of_X = -1
    ofX *= -1
sign_of_C = +1
if ofC < 0:
    sign_of_C = -1
    ofC *= -1

if debug:
    print('ofX = {} and ofC = {}'.format(ofX, ofC))
    print('sgX = {} and sgC = {}'.format(sign_of_X, sign_of_C))

sign_of_C *= sign_of_X
sign_of_X *= sign_of_X

if the_gcd(ofX, ofC) != 0:
    aaa = sign_of_C * ofC / the_gcd(ofX, ofC)

    bbb = sign_of_X * ofX / the_gcd(ofX, ofC)

if ofX == 0:
    print('invalid')
else:
    print('{} {}'.format(int(aaa), int(bbb)))

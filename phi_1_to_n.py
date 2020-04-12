# with sum of divisors property
def sum_phi_to(n):
    res = [int(x-1) for x in range(n+1)]
    res[0] = 0
    res[1] = 1
    for i in range(2,n+1):
        for j in range(2 * i, n+1, i):
            res[j] -= res[i]
    return res


# with sieve of eratosthenes
def sieve_phi_to(n):
    res = [int(x) for x in range(n+1)]
    for i in range(2, n+1):
        if res[i] == i:
            for j in range(i, n+1, i):
                res[j] -= res[j] // i
    return res


print(sieve_phi_to(20))
print(sum_phi_to(20))


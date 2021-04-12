def Myfun(N):
    if N == 1:
        return 1
    else:
        return N * Myfun(N-1)


print(Myfun(5))


def add(n):
    if n == 1:
        return 0
    else:
        return n + add(n - 1)


print(add(10))

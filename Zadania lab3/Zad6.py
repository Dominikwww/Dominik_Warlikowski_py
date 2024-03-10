def IloczynElementowCiagu(a=1, b=4, ile=10):
    res = a
    for x in range(0, ile):
        a *= b
        res *= a
    return res


print(IloczynElementowCiagu(1, 2, 3))

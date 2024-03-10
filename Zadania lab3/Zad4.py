def CzyProstokatny(a, b, c):
    if (a**2+b**2 == c**2) | (a**2+c**2 == b**2) | (c**2+b**2 == a**2):
        return 1
    else:
        return 0


print(CzyProstokatny(3, 4, 5))

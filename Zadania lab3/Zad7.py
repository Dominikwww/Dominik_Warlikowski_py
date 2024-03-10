import math

try:
    l1 = int(input('Liczba: '))
    print(math.sqrt(l1))
except ValueError:
    print('Error')

import random

listy1 = [random.randint(0, 100) for x in range(0, 10)]
print(listy1)
listy2 = [x for x in listy1 if x % 2 == 0]
print(listy2)

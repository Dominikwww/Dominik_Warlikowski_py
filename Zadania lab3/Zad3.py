s1 = {'chleb': 'szt', 'wiogrona': 'kg'}
s2 = {v: k for v, k in s1.items() if k == 'szt'}
print(s2)

# a = 56
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# zmienna_tekstowa = 'Wizuazlizacja danych'
# print(zmienna_tekstowa)
# print(type(zmienna_tekstowa))

# a = 3
# b = 5
# c = a*b
# print(c)
# c = pow(a, b)
# print(c)
#
# i = 6 ** (1/2)
# print(i)
# i = pow(6, 1/2)
# print(i)
#
# k = 'test'
# k2 = 'test2'
# m = 2
# print(k+' '+k2+'\n'+str(m))

# a = 5
# b = 3.33
# print('liczba a jest równa {:d} {:.2f}'.format(a, b))

# a = input('Wpisz liczbę: ')
# a = int(a)
# print(5*a)
# print(type(a))

# sys.stdout.write('Wprowadz liczbe: ')
# b = sys.stdin.readline()  # dodaje na końcu \n
# print(b)
# print(type(b))

lista = [5, 4, 3, 5, 6, 'a', 'b', [1, 2, 3, 1], 'kkk', 'test']
print(lista)
lista.append(67)
print(lista)
lista.insert(2, 'c')
print(lista)
lista.extend(['3', 3, 4, 6, 1])
print(lista)
lista.pop(2)
print(lista)
lista.pop()
print(lista)
lista.remove(3)
print(lista)
del lista[1]
print(lista)
# del lista
# print(lista)
lista.reverse()
print(lista)
# lista.sort()
# print(lista)

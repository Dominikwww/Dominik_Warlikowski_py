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

# lista = [5, 4, 3, 5, 6, 'a', 'b', [1, 2, 3, 1], 'kkk', 'test']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(2, 'c')
# print(lista)
# lista.extend(['3', 3, 4, 6, 1])
# print(lista)
# lista.pop(2)
# print(lista)
# lista.pop()
# print(lista)
# lista.remove(3)
# print(lista)
# del lista[1]
# print(lista)
# # del lista
# # print(lista)
# lista.reverse()
# print(lista)
# # lista.sort()
# # print(lista)

# slownik = {'klucz': 'wartosc', 1: 2, 'a': 1, 4: 'b', 1: 4}
# print(slownik)
# print(slownik[1])
# slownik[3] = 'aaa'
# print(slownik)
# slownik.pop(4)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik['a']
# print(slownik)

# a = 6
# b = 7
#
# if a > b:
#     print(a)
# elif a == b:
#     print(a+2*b)
# else:
#     print(b)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print(b, d)

# for i in range(2, 8, 2):
#     print(i)
# else:
#     print('koniec')

# for i in lista:
#     print(i)

# for i in range(0, 5):
#     for j in range(0, 5):
#         result = i+j
#         print(result)
#     print('')

# licznik = 0
# while licznik < len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print('\nKONIEC')

# licznik = 0
# while licznik != 10:
#     if licznik == 7:
#         print(licznik)
#         break
#     else:
#         licznik += 1
# else:
#     print('licznik')

lista = [1, 2, 44, 33, 11, 15, 7, 22]
zm = int(input('liczba: '))
licznik = 0
while licznik < len(lista):
    if zm - lista[licznik] == 0:
        print('jest 0')
        break
    else:
        licznik += 1
else:
    print('nie ma')

# if zm in lista:
#     print('jest')
# else:
#     print('nie ma')

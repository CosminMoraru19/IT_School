#Versiunea in Romana

# from math import pi

#1 --Funcție care să calculeze și să returneze suma a două numere
#
# def suma(a, b):
#     suma = a + b
#     print(suma)
# suma(1, 3)
# suma(13, 5)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 2-- Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# def check(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return  False
#
#
# print(check(3))
# print(check(2))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3 -- Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)


# def numarul():
#     x = str(input("Numele compler:\n"))
#     counter = 0
#     for i in range(len(x)):                          # de intreabat cum pun intr-un loop toata trebaa asta, adica sa ma puna sa completez la nesfarsit numele pana orepsc
#         if x[i] == ' ':
#             continue
#         counter = counter +1
#     return counter
#
#
# print(numarul())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 4-- Funcție care returnează aria dreptunghiului


# def arie_dreptunghiului():
#     a = int(input('L = \n'))
#     b = int(input('l = \n'))
#     return a * b
#
#
# print(arie_dreptunghiului())



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#5-- Funcție care returnează aria cercului



# def aria_cerc():
#     r = int(input('R = \n'))
#     aria = pi * r * r
#     return aria
#
#
# print(aria_cerc())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# # 6 -- Funcție care returnează True dacă un caracter x se găsește într-un string datși False dacă nu găsește.



# def caractere():
#     x = str(input('Sir de caractere= \n'))
#     n = str(input('Caracterul de gasit = \n'))
#     for i in range(len(x)):
#         if x[i] == n or x[i] == n.upper() or x[i].upper()  == n:
#             print(True)
#             break
#         else:
#             print(False)
#         break
#
#
# caractere()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#7 -- Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y


# def numar_caratere():
#     x = str(input('Sir de caractere= \n'))
#     upcar = 0
#     lowcar = 0
#     for i in range(len(x)):
#         if x[i] == x[i].lower():
#             if x[i] == ' ':
#                 continue
#             lowcar = lowcar + 1
#         elif x[i] == x[i].upper():
#             upcar = upcar + 1
#     print(f'low Characters are {lowcar}')
#     print(f'upper characters are  {upcar}')
#
#
# numar_caratere()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#8 -- Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive


# def lista_numere_pozitive():
#     list1 = []
#     list2 = []
#     n = int(input("Cate numere introducem \n"))
#     for i in range(0,n):
#         element = int(input(' Numar de introdus in lista\n'))
#         list1.append(element)
#     print(f'Lista cu toate numerele este {list1}')
#     for y in range(len(list1)):
#         if list1[y] < 0:
#             continue
#         else:
#             list2.append(list1[y])
#     print(f'lista doar cu numere pozitive este {list2}')
#
#
# lista_numere_pozitive()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 9 -- Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.



# def nimic(x,y):
#     if x>y:
#         print(f'Primul numar este mai mare}')
#     elif x<y:
#         print(f'Al doilea numar este mai mare')
#     else:
#         print(f'Numerele sunt egale')
#
# nimic(2,3)    #incercare sa vedem daca programul fucntioneaza ok
# nimic(a,4)    #incercare sa veden daca programul da eroare



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 10 -- Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False


# def functie():
#     x = int(input('Numar de verificat= \n'))
#     set1 = {4,6,8,10,12,5}
#     for i in range(len(set1)):
#         if x not in set1:
#             set1.add(x)
#             print(f'Am adaugat numarul {x} in set')
#             print(set1)
#             return True
#
#         elif x in set1:
#             print(f'nu am adaugat numarul {x} in set. Acesta deja exista')
#             print(set1)
#             return False
#
#
# print(functie())



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# Exercitii optionale

# 1 -- Funcție care primește o lună din an și returnează câte zile are acea luna



import calendar
from calendar import monthrange
# def Calendar():
#     c = calendar.TextCalendar(calendar.MONDAY)
#     str = c.formatmonth(2022, 2, 0, 0)
#     for i in c.itermonthdays(2022, 2):
#         print(i)
#
# Calendar()

# def zile_ale_lunii(an, luna):
#     return monthrange(an, luna)[1]
#
#
# print(zile_ale_lunii(2016, 2))



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#2 -- Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

        # În final vei putea face:
        # a, b, c, d = calculator(10, 2)
        # ● print("Suma: ", a)
        #
        # ● print("Diferenta: ", b)
        # ● print("Inmultirea: ", c)
        # ● print("Impartirea: ", d)

# from operator import add, sub, mul, floordiv
# def calculator(a, b, *functii):
#     for x in functii:
#         print(f'{x.__name__}={x(a,b)}')
# a, b = (10, 2)
# calculator(a, b, add, sub, mul, floordiv)
#
# ------------------------------------------------------
# def calculeaza(a, b):
#     suma = a + b
#     diferenta = a - b
#     inmultirea = a * b
#     impartirea = a / b
#     return suma, diferenta, inmultirea, impartirea
#
# a, b, c, d = calculeaza(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 3 -- Funcție care primește o lista de cifre (adică doar 0-9)
        # Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
        # Returnează un DICT care ne spune de câte ori apare fiecare cifră
        # => dict {
        # 0: 0
        # 1 :2
        # 2: 0
        # 3: 1
        # 4: 0
        # 5: 3
        # 6: 0
        # 7: 2
        # 8: 0
        # 9: 1
        # }

# Versiunea 1:


# import json
# def digit_count(*digits):
#     count = {}
#     for digit in digits:
#         if digit in count:
#             count[digit] += 1
#         else:
#             count[digit] = 1
#     return count
#
# print(json.dumps(digit_count(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0), indent=4))


#Varsiunea 2:

# import json
# def numara_cifre(*lista_cifre):
#     dict_cifre = {i: 0 for i in range(10)}
#     for cifra in lista_cifre:
#         dict_cifre[cifra] += 1
#     return dict_cifre
#
#
# print(json.dumps(numara_cifre(2, 3, 4, 2, 2, 4, 5, 6, 2), indent=4))


# Versiunea 3:

# 13C
# def numar_aparitii(lista_cifre):
#     dict_cifre = {i: 0 for i in range(10)}  # initializam dictionarul cu toate cifrele si 0 aparitii
#     for cifra in lista_cifre:
#         dict_cifre[cifra] += 1  # incrementam numarul de aparitii al cifrei
#     return dict_cifre
#
#
# lista_cifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# dict_aparitii = numar_aparitii(lista_cifre)
# print(dict_aparitii)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#4 -- Functie care primeste 3 numere.  Returneaza valoarea maxima dintre ele


# Versiunea 1:


# def maximul(x, y, z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     else:
#         return z
# #
# #
# print(maximul(1,4,3))
# print(maximul(10,2,4))
# print(maximul(1,32,425))


#Versiunea 2:

# def max_sum(num1, num2, num3):
#     return max(num1+num2, num2+num3, num1+num3)
#
#
# print(max_sum(2, 10, 43))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#5 -- Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
        # Ex: daca dam nr 3
        # Suma va fi 6 (0+1+2+3)

# Versiunea 1:


# def suma(n):
#     rezultat = 0
#     for i in range(1, n+1):
#         rezultat = rezultat + i
#     print(rezultat)
#
# suma(5)

# Versiunea 2:


# def sum_to_n(n):
#     return sum(range(n+1))
#
#
# print(sum_to_n(7))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercitii bonus



# 1 -- Functie care primesete 2 liste de numere (numerele pot fi dublate)
        # Returnati numerele comune
        #
        # Ex:
        # list1 = [1, 1, 2, 3]
        # list2 = [2, 2, 3, 4]
        # Raspuns: {2, 3}


# def numere_comune(lista1, lista2):
#     numere_comune = []
#     for numar in lista1:
#         if numar in lista2 and numar not in numere_comune:
#             numere_comune.append(numar)
#     return numere_comune
#
#
# lista1 = [1, 2, 3, 4, 5, 5]
# lista2 = [4, 5, 6, 7, 8, 5]
#
# numere_comune = numere_comune(lista1, lista2)
# print(numere_comune)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2 -- Functie care sa aplice o reducere de pret
        # Daca produsul costa 100 lei si aplicam reducere de 10%
        # Pretul va fi 90
        # Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida


# def aplica_reducere(pret, reducere):
#     if reducere <= 0 or reducere >= 100:
#         return pret
#     else:
#         pret_redus = pret * (1 - reducere / 100)
#         return round(pret_redus, 2)
#
#
# print(aplica_reducere(600, 45))



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 3 -- Functie care sa afiseze data si ora curenta din ro  (bonus: afisati si data si ora curenta din China)


# import datetime
# import pytz
#
# def display_current_time():
#     timezone_ro = pytz.timezone('Europe/Bucharest')
#     now_ro = datetime.datetime.now(timezone_ro)
#     print(f'Ora curenta in Romania: {now_ro.strftime("%Y-%m-%d %H:%M:%S")}')
#
#     timezone_cn = pytz.timezone('Asia/Shanghai')
#     now_cn = datetime.datetime.now(timezone_cn)
#     print(f'Ora curenta in China: {now_cn.strftime("%Y-%m-%d %H:%M:%S")}')
#
#
# display_current_time()



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 4 --  Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

# import datetime
#
# def zile_pana_la_craciun():
#     ziua_craciunului = datetime.date(datetime.date.today().year, 12, 25)
#     azi = datetime.date.today()
#     zile_ramase = (ziua_craciunului - azi).days
#     return zile_ramase
#
#
# zile_ramase = zile_pana_la_craciun()
# print(f'Mai sunt {zile_ramase} zile până la Crăciun!')
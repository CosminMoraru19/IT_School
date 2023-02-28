#Versiunea in Romana
import random

#1 -- .Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.


# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# i = 0
# masina = input('Masina \n')
# for i in masini:                          #for normal
#     print(f'Masina mea preferata este {i}')
# for masina in masini:                             #for each
#     print(f'Masina mea prefera este {masina}')
    # if masina == 'Volvo':
    #     break
    # print(f'Masina mea preferata este  {masina}')

# while i < len(masini):
#     print(f'Masina mea preferata este  {masini[i]}')         # cu while
#     i = i+1


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#2-- 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.



# masini = ['Audi', 'Volvo', 'bmw', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# # masini_upper = []
# lungime_sir= len(masini)
# for i in range(lungime_sir-1):
#     masini[i] = masini[i].upper()
#     i = i + 1
#     masini[0] = masini[0]. lower()
# else:
#    masini[lungime_sir-1] = masini[lungime_sir-1].lower()
# print(masini)

# print(masini)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#3 -- # Aceeași listă:
    # Vine un cumpărător care dorește să cumpere un Mercedes.
    # Itereaza prin ea prin modalitatea aleasă de tine.
    # Dacă mașina e mercedes:
    # Printează ‘am găsit mașina dorită de dvs’
    # Ieși din ciclu folosind un cuvânt cheie care face acest lucru
    # Altfel:
    # Printează ‘Am găsit mașina X. Mai căutam‘



# masini = ['Audi', 'Volvo', 'bmw', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
# masina = input('Masina dorita \n')
# # i = 0
# for i in range(len(masini)):
#     if masini[i] == masina:
#         print("Am gasit masina dorita de dumneavoastra")
#         break
#     else:
#         print(f'Am gasit masina {masini[i]}. Mai cautam')
# else:
#     print(f'Masina nu se afla in stock')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#4-- Aceași listă;
    # Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
    # excepția Trabant și Lăstun.
    # - Dacă mașina e Trabant sau Lăstun:
    # Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
    # else).
    # - Printează S-ar putea să vă placă mașina x.



# masini = ['Audi', 'Volvo', 'bmw', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
# # i = 0
# for i in range(len(masini)+1):
#     if masini[i]=='Trabant' or masini[i]=='Lastun':
#         # masini.remove(masini[i])
#         continue
#     print(f's-ar putea sa va placa {masini[i]}')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#5 -- Modernizează parcul de mașini:
    # ● Crează o listă goală, masini_vechi.
    # ● Itereaza prin mașini.
    # ● Când găsesti Lăstun sau Trabant:
    # - Salvează aceste mașini în masini_vechi.
    # - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
    #
    # ● Printează Modele vechi: x.
    # ● Modele noi: x.


# masini = ['Audi', 'Volvo', 'bmw', 'Mercedes', 'Aston Martin', 'Lastun','Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
# print(f'Modele noi {masini}')
# print(f'Modele vech {masini_vechi}')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#6-- Având dict:
    # pret_masini = {
    # 'Dacia': 6800,
    # 'Lăstun': 500,
    # 'Opel': 1100,
    # 'Audi': 19000,
    # 'BMW': 23000
    # }
    # Vine un client cu un buget de 15000 euro.
    # ● Prezintă doar mașinile care se încadrează în acest buget.
    # ● Itereaza prin dict.items() și accesează mașina și prețul.
    # ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
    # xLastun
    # ● Iterează prin listă.



# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# list = []
# for key,value in pret_masini.items():
#     if value <= 15000:
#         #continue
#         list.append({key})
#         print(f'Pentru un buget de sub 15000 euro puteti alege masina de {value} marca {key}')
# print(list)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#7 -- Având lista:
    # numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
    # ● Iterează prin ea.
    # ● Afișează de câte ori apare 3 (nu ai voie să folosești count).


# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Trei = 0
# for i in numere:
#     if i == 3:
#         Trei = Trei+1
# print(f'Trei apare de {Trei} ori in lista')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#8-- Aceeași listă:
    # ● Iterează prin ea
    # ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).


# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma_numerelor = 0
# for i in range(len(numere)):
#     suma_numerelor = suma_numerelor+numere[i]
# print(suma_numerelor)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#9 -- Aceeași listă:
    # ● Iterează prin ea.
    # ● Afișază cel mai mare număr (nu ai voie să folosești max).


# numere = [5, 7, 3, 9, 3, 3, 1, 0, 10,1,5,102]
# i = 0
# numarul_maxim = 0
# for i in range(len(numere)-1):
#     if numere[i] < numere[i+1]:
#         numarul_maxim = numere[i+1]
#         # continue           not apllicable
#     # print(numarul_maxim)   not applicable
# print(numarul_maxim)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#10 -- 10. Aceeași listă:
    # ● Iterează prin ea.
    # ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
    # Ex: dacă e 3, să devină -3
    # ● Afișază noua listă.


# numere = [5, 7, 3, 9, 3, 3, -1, 0, 10,1,5,-10]
# i = 0
# for i in range(len(numere)):
#     numere[i] = numere[i] * (-1)
# print(numere)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Exercitii optionale
# #1 -- alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
        # numere_pare = []
        # numere_impare = []
        # numere_pozitive = []
        # numere_negative = []
        # Itereaza prin listă alte_numere
        # Populează corect celelalte liste
        # Afișeaza cele 4 liste la final



# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# i = 0
# for i in range(len(alte_numere)):
#     if alte_numere[i]%2 == 0 and alte_numere[i] > 0:
#         numere_pare.append(alte_numere[i])
#     elif alte_numere[i]%2 != 0 and alte_numere[i] > 0:
#         numere_impare.append(alte_numere[i])
#     elif alte_numere[i] < 0:
#         numere_negative.append(alte_numere[i])
#
# numere_pozitive = numere_pare+numere_impare
# print(numere_pare)
# print(numere_impare)
# print(numere_negative)
# print(numere_pozitive)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2 -- Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.


# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# for i in range(len(alte_numere)):
#     for j in range(i+1 , len(alte_numere)):
#
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[i],alte_numere[j] = alte_numere[j], alte_numere[i]
# print(alte_numere)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#3 -- Ghicitoare de număr:
    # numar_secret = Generați un număr random între 1 și 30
    # Numar_ghicit = None
    # Folosind un while
    # User alege un număr
    #
    # Programul îi spune:
    # ● Nr secret e mai mare
    # ● Nr secret e mai mic
    # ● Felicitări! Ai ghicit!

# import random
#
# numar_secret = random.randint(0,30)
# print(numar_secret)
# numar_ghicit = int(input('alege un numar'))
# while numar_secret != numar_ghicit:
#     if numar_ghicit < numar_secret:
#         print('Numarul secret este mai mare')
#         numar_ghicit = int(input('alege un numar'))
#     elif numar_ghicit > numar_secret:
#         print('Numarul secret este mai mic')
#         numar_ghicit = int(input('alege un numar'))
#     elif numar_ghicit == numar_secret:# numar_ghicit==numar_secret:
#         break
#     print('Ai ghicit numarul')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#4  -- Alege un număr de la tastatură
        # Ex: 7
        # Scrie un program care să genereze în consolă următoarea piramidă
        # 1
        # 22
        # 333
        # 4444
        # 55555
        # 666666
        # 7777777



# numar=int(input('Numarul:'))
# i=1
# j=0
# while i<=numar:
#     while j<i:
#         print(i,end='')
#         j+=1
#     print('\r')
#     j=0;
#     i+=1


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#5 -- tastatura_telefon = [
        # [1, 2, 3],
        # [4, 5, 6],
        # [7, 8, 9],
        # [0]
        # ]
        # Iterează prin listă 2d
        # Printează ‘Cifra curentă este x’
        # (hint: nested for - adică for în for)

# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
#
# for i in range(len(tastatura_telefon)):  # index i folosit pentru a itera prin prima lista
#     for j in range(len(tastatura_telefon[i])):  # index j folosit pentru a itera prin fiecare din subliste
#         print(f"Cifra curenta este {tastatura_telefon[i][j]}") # printeaza fiecare element din fiecare lista, pe rand si pe orizontal


#Romanian language version.

#1 -- Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else

# Functia If este o fucntie care poate returna 2 sau mai multe rezultate diferite, in furnctie de o conditie presetata.
# Daca argumentul este adevarat acesta va genera rezultatul dorit, daca arguemntul este fals, atunci va sari peste actiune.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 2--Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)


# x = 'safdf'
# if type(x) == int and x>0:
#     print(f'Numarul {x} este intreg')
# else:
#     print(f'Numarul {x} nu este intreg')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#3--- Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru


# x = int(input('Numar:'))
# if x > 0:
#     print(f'{x} este pozitiv')
# elif x < 0:
#     print(f'{x} este negativ')
# else:
#     print(f'{x} este neutru')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#4-- Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).


# x = int(input('Numar:'))
# if x > -2 and x < 13:
#     print(f'{x} se afla in interval')
# else:
#     print(f'{x} nu se afla in interval')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#5-- Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
#              cate numere sunt intre x si y, nu rezultatul diferentei intre x si y).


# x = int(input('x='))
# y = int(input('y='))
# if x-y < 5:
#     print(f'Diferenta dintre numere este mai mica decat 5')
# else:
#     print(f'Diferenta dintre numere nu este mai mica decat 5')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#6-- Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

#
# x = int(input('x='))
# if not( x>= 5 and x <= 27):
#     print(f' {x} nu se afla in itnerval')
# else:
#     print(f' {x}  se afla in itnerval')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#7 -- Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
#         daca nu, afiseaza care din ele este mai mare



# x = int(input('x='))
# y = int(input('y='))
# if x == y:
#     print(f'Numerele sunt egale')
# elif x>y:
#     print(f'x este numarul mai mare')
# else:
#     print(f'y este mai mare')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#8 -- Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
#           triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
#               oarecare (nicio latura nu e egala).


# x= int(input('x='))
# y= int(input('y='))
# z= int(input('z='))
# if x == y == z:
#     print(f'Triunghiul cu laturile x,y,z este isoscel')
# elif (x == y or y == z or x == z) and (x != z or x != y or y != z or y != x or z != x or z != y):
#     print(f'Triunghiul cu laturile x,y,z este echilateral')
# else:
#     print(f'Triunghiul cu laturiel x,y,z este oarecare')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#9--  Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
#           Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.



# x = input('Litera=')
# if x == 'a' or x == 'A':
#     print(f'{x} este vocala')
# elif x == 'e' or x == 'E':
#     print(f'{x} este vocala')
# elif x == 'o' or x =="O":
#     print(f'{x} este vocala')
# elif x == 'i' or x =='Y':
#     print(f'{x} este vocala')
# elif x == 'u' or x =='U':
#     print(f'{x} este vocala')
# else:
#     print(f'{x} nu este vocala')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#10 -- Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
                # a. Peste 9 => A
                # b. Peste 8 => B
                # c. Peste 7 => C
                # d. Peste 6 => D
                # e. Peste 4 => E
                # f. 4 sau sub => F



# x = int(input('Nota='))
# if x >= 9:
#     print(f'Nota A')
# elif x >= 8 and x < 9:
#     print(f'Nota B')
# elif x >= 7 and x < 8:
#     print(f'Nota C')
# elif x >= 6 and x < 7:
#     print(f'Nota D')
# elif x >= 4 and x < 6:
#     print(f'Nota E')
# elif x < 4:
#     print(f'Nota F')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Exercitii optionale:

#1 --  Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)


# x = 12
# if x.bit_count() >= 4:
#     print(f'{x} are minim 4 cifre')
# else:
#     print(f'{x} nu are minim 4 cifre')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 2 -- Verifica daca x are exact 6 cifre


# x = 123456
# if x.bit_count() == 6:
#     print(f'{x} are 6 cifre')
# else:
#     print(f'{x} nu are 6 cifre')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#3 -- Verifica daca x este numar par sau impar

# x = 12343
# if x%2 == 0:
#     print(f'{x} este par')
# else:
#     print(f'{x} este impar')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#4 -- Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele


# x = int(input('x='))
# y = int(input('y='))
# z = int(input('z='))
#
# if x > y and x > z:
#     print(f'x este cel mai mare numar')
# elif y > x and y > z:
#     print(f'y este cel mai mare numar')
# else:
#     print(f'z este cel mai mare numar')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 5 -- Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
    # triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
    # 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
    # lungimea celei de-a treia laturi)


# AB= int(input('AB='))
# BC= int(input('BC='))
# AC= int(input('AC='))
#
# if AB + BC + AC == 180 and AB > 0 and BC > 0 and AC > 0:
#     print(f'Triunghoul format din laturile AB,AC si BC este valid')
# else:
#     print(f'Triunghoul format din laturile AB,AC si BC nu este valid')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#6 --  Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
    # la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
    # ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
    # smarte'


# Sir = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('x='))
# print(Sir[0:-x])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 7-- Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format  din primele 5 caractere + ultimele 5


# Sir = str('Coral is either the stupidest animal or the smartest rock')
# PrimaParteString = Sir[0:5]
# DimSirFaraUltimele5 = len(Sir)-5
# UltimaParteString = Sir[DimSirFaraUltimele5:]
# # print(UltimaParteString)
# SirNou = PrimaParteString+' acesta este un si nou ' +UltimaParteString
# print(SirNou)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#8 -- Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '

# x = 'Coral is either the stupidest animal or the smartest rock'
# y = len(x) - 4
# z = x[y:]
# print(x[:y])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#9 -- Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# functie pentru a face string-ul case insensitive)


# x = input('Scrie un cuvant: ').upper()
# assert x[0] == x[-1]
# print('corect')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 10-- Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

# x = '0123456789'
# print(x[2::2], x[1::2])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercitii bonus!

#1-- Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
# inputuri urmatoarele informatii:
        # a. Varsta
        # b. Insotit de mama
        # c. Insotit de tata
        # d. Pasaport
        # e. Act permisiune mama
        # f. Act permisiune tata
# Conditii de imbarcare:
        # 1. Daca pers are varsta peste 18 ani si are pasaport
        # 2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
        # 3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
        # si are permisiune in scris de la celalat parinte
#
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
# variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
# apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
# Exemple:
    # 1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
    # 2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca



# a = int(input('Varsta: '))
# b = input('Insotit de mama? (da/nu) ')
# c = input('Insotit de tata? (da/nu) ')
# d = input('Pasaport (da/nu) ')
# e = input('Act permisiune mama? (da/nu) ')
# f = input('Act permisiune tata? (da/nu) ')
# if a >= 18 and d == 'da':
#     print(f'Varsta {a} ani, am pasaport => Ma pot imbarca')
# elif a < 18 and d == 'da' and c == 'da' and b == 'da':
#     print(f'Varsta {a} ani, am pasaport, ambii parinti, fara acte de permisiune => Ma pot imbarca')
# elif a < 18 and d == 'da' and (b == 'da' and f == 'da') or (c == 'da' and e == 'da'):
#     print(f'Varsta {a} ani, am pasaport, cel putin un parinte si actul de permisune al celuilalt => Ma pot imbarca')
# else:
#     print('Nu ma pot imbarca fie din lipsa pasaportului, a unui parinte sau a unui act de permisiune in cazul in care sunt minor/a')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2-- Joc de noroc

# - Cauta pe net si vezi cum se genereaza un numar random
# - Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
# Numarul salvat va fi generat random cu metoda gasita in online
# - Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
# - Verifica si afiseaza daca utilizatorul a ghicit numarul
# - Vor exista 3 optiuni care vor trebui tratate:
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari? Ai ales x si zarul a fost y


# import random
# dice_roll = (random.randint(1, 6))
# x = int(input('Alege un numar: '))
# if x == dice_roll:
#     print(f'Ai ghicit! Felicitari! Ai ales {x} si zarul a fost {dice_roll}')
# elif x > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
# else:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
# Romanian language version.
# 1 -- În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

# O variabila este o valoare presetata de utilizator si memorata de catre calculator pentru a o uitiliza de fiecare data cand este accesata.


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 2 --- Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă :

# Nume = 'Cosmin'
# Varsta = 26
# Media_generala = 8.32
# Admis = True

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 3 -- Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

# print(type(Nume))
# print(type(Varsta))
# print(type(Media_generala))
# # print(type(Admis))


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #  4 -- Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
#               - Verifică tipul acesteia.

# print(round(Media_generala))
# print(type(round(Media_generala)))
# Media_generala=round(Media_generala)
# print(Media_generala)
# print(type(round(Media_generala)))



# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #5 -- Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.

# print('Varsta mea este '+ str(Varsta))
# print(f'Am terminat cu media generala {Media_generala}')
# print(f'Numele meu este {Nume}, am varsta de {Varsta}, media generala fiind {Media_generala} statul meu de Admis fiind {Admis}')


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #6 -- Citește de la tastatură:
#               - numele;
#               - prenumele.
#              Afișează: 'Numele complet are x caractere'.


# Nume = input('Nume: ')
# Prenume = input('Prenume:')
# print(f'Numele intreg are {len(Nume)+len(Prenume)} caractere')



# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 7 -- Citește de la tastatură:
#       - lungimea;
#       - lățimea.
#         Afișează: 'Aria dreptunghiului este x'.

# Lungime = int(input('Lungime: '))
# Latime = int(input('Latime: '))
# print(f'Aria dreptunghiului este {Lungime*Latime}')


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #8 -- Având stringul: 'Coral is either the stupidest animal or the smartest rock':
#              - afișează de câte ori apare cuvântul 'the';


# Fraza = 'Coral is either the stupidest animal or the smartest rock'  #rezolvat
# print(Fraza.count(' the '))


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 9 --Același string.
#            Afișează de câte ori apare cuvântul 'the';
#            Printează rezultatul.


 # Fraza = 'Coral is either the stupidest animal or the smartest rock'
 # print(Fraza.replace(' the ', ' THE '))


# Exercitii optionale.

# 1 -- Citește de la tastatură un string de dimensiune impară;
#        - afișează caracterul din mijloc.

#Prima versiune:

# Nume = input('Nume')
# print(f'Caracterul din mijloc este {Nume[(len(Nume)//2)]}')

# A doua versiune:

# sir = str(input('Insert string with odd character length: '))
# lungime_sir = len(sir)
# if sir % 2 != 0:
#     sir_impartit = lungime_sir // 2
#     print('Caracterul din mijlloc este:', sir[sir_impartit])
#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2 -- Folosind assert, verifică dacă un string este palindrom.

# Cuvant = input('Intodu cuvantul:')
# Cuvant_inversat = str(Cuvant[::-1])
# assert Cuvant == Cuvant_inversat
# print("Cuvantul este palindrom")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 3 -- Exercițiu:
#           - citește un string de la tastatură (ex: alabala portocala);
#           - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
#           - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.


# Fraza = input("Fraza:")
# # Fraza = 'alabala portocala'
# Variabila = Fraza[0]
# # print(Variabila)
# Litera_mare=Variabila.upper()
# # print(Litera_mare)
# Fraza_majuscule = Fraza.replace(Fraza[0],Litera_mare)
# print(Fraza_majuscule)
# Variabila_majuscula = Fraza_majuscule[0]
# Litera_mica = Variabila_majuscula.lower()
# # print(Litera_mica)
# Final=Fraza_majuscule.replace(Fraza_majuscule[0],Litera_mica)
# print(Final)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 4-- Exercițiu:
#       - citește un user de la tastatură;
#       - citește o parolă;
#        - afișează: 'Parola pt user x este ***** și are x caractere';
#           - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.


# User= input("User:")
# Parola = input("Parola:")
# Lungime_parola = len(Parola)
# print(f'Parola pentru Userul {User} este {Lungime_parola * "*"}  si are {len(Parola)} caractere')

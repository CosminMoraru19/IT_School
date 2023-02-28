# Versiune limba romana


# 1. -- Declara o lista note_muzicale in care sa pui do re mi etc pana la do
    # a. Afiseaz-o
    # b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
    # varianta actuala (inversata)
    # c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
    # inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
    # asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
    # varianta inițială
# Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
#   suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
#   suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
#   găsesc utilitatea în funcție de ce ne dorim in acel moment.


from typing import List

# note = ['do', 're', 'mi', 'fa','sol','la','si','do']
# print(note)    #a
# note = note[::-1]   #b
# print(note)
# note.reverse()  #c
# print(note)     #d


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2 -- Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
# note = ['do', 're', 'mi', 'fa','sol','la','si','do']
# do = note.count('do')
# print(do)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#3 -- Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.

# lista1 = [3,1,0,2]
# lista2 = [6,5,4]
# lista_intreaga = lista1+lista2
# print(lista_intreaga)
# lista1.extend(lista2)
# print(lista1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#4-- Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
#           folosind o functie si apoi afiseaza din nou lista



# lista_intreaga.sort()
# print(lista_intreaga)
# del lista_intreaga[0]
# print(lista_intreaga)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 5 -- Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
#       - Lista este goala (IF)
#       - Lista nu este goala (ELSE)


# if len(lista_intreaga) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#6 -- Foloseste o functie care sa goleasca lista de la exercitiul 3


# lista_intreaga.clear()
# print(lista_intreaga)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 7-- Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se afiseze ca lista e goala


# if len(lista_intreaga) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 8 -- Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa afisezi Elevii (cheile)


# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# print(dict1.keys())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 9--  Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
#       Ex: ‘Ana a luat nota {x}’.
#       Doar nota o vei lua folosindu-te de cheie


# x = dict1.get('Ana')
# print(f'Ana a luat nota {x}')
# y = dict1.get('Gigel')
# print(f'Gigel a luat nota {y}')
# z = dict1.get('Dorel')
# print(f'Dorel a luat nota {z}')




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#10 -- Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# - Modifica nota lui Dorel in 6
# - Printeaza nota lui dupa modificare


# dict1['Dorel'] = 6
# print(dict1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 11 -- Imagineaza-ti ca Gigel se transfera din clasa.
    # - Cauta o functie care sa il stearga
    # Vine un coleg nou.
    # - Adaugati-l in lista pe Ionica, cu nota 9
    # - Printati dictionarul cu noii elevi

#del dict1['Gigel']
# print(dict1)
# dict1.update({'Ionica':9})
# print(dict1)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 12-- Ai urmatoarele seturi:
    # zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
    # weekend = {'sambata', 'duminica'}
    # - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
    # - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.



# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)    #nu se intampla nimic deoarece in seturi nu putem avea duplicari



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#13 -- Foloseste un if si verifica daca:
    # - Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
    # regasesc intre elementele din setul zile_sapt)
    # - Weekend nu este un subset al zilelor din sapt
    # Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
    # punct de mai sus va fi un boolean


# if weekend.issubset(zile_sapt):
#     print('Weekend este subset al zilelor saptamanii')     #maybe not right
# else:
#     print('Weekend nu este subset al zilelor saptamanii')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#14 -- Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu sunt in weekend si invers)


# difset = zile_sapt-weekend
# print(f'diferenta dintre cele dosu seturi este {difset}')
# diferenta = zile_sapt.difference(weekend)
# print(diferenta)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





# 15 -- Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in ambele seturi). Hint: Va puteti folosi de o functie


# elemente_comune = weekend.intersection(zile_sapt)
# print(elemente_comune)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#Exercitii optionale

# 1 --   Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
    # - Declara o lista cu 5 jucatori: lista_jucatori_teren
    # - Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
    # - Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
    # - Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
    # - SCHIMBARI_MAX va fi o constanta cu valoarea 3
    # Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
    # - Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
    # teren
    # - Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
    # - Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
    # de rezerva
    # - Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
    # variabilelor voastre)
    # Daca jucatorul pe care vrem sa il schimbam nu e in teren:
    # - Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
    # Altfel, afisati ecran: ‘mai aveti z schimbari’




#prima versiune
# lista_jucatoru_teren = ['Cosmin','Mihai','Marian','Alberto','Paul']
# lista_jucatori_rezerva = ['Roberto','Costel','Dorin','Doru','Daniel']
# lista_jucatori_scosi = []
# Schimbari_maxim = 3
# Schimbari_efectuate = 0
#
# for x in lista_jucatori_rezerva:
#     if x in lista_jucatoru_teren or Schimbari_maxim >= 1:
#         lista_jucatori_scosi.insert(0,lista_jucatori_teren.remove(0))
#         print(f'A iesit jucatorul {lista_jucatoru_teren.pop(0)}')
#         print(f'A iesit jucatorul {lista_jucatori_scosi(0)}')
#         print(f' mai aveti {Schimbari_maxim = Schimbari_maxim-1}')
#         print(f'S-au efectuat {Schimbari_efectuate=Schimbari_efectuate+1) schimbari)
#     else:
#         print(f'Scimbarea nu se paote efectua')

# a doua versiune
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 1
# SCHIMBARI_MAX = 3
# x = str(input('Iese de pe teren: \n'))
# y = str(input('Intra pe teren: \n'))
# z = SCHIMBARI_MAX - schimbari_efectuate
#
# # for x in lista_jucatori_teren or y in lista_jucatori_rezerva:
# if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#     lista_jucatori_teren.remove(x)
#     lista_jucatori_rezerva.remove(y)
#     lista_jucatori_scosi.append(x)
#     lista_jucatori_teren.append(y)
#
#     print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
#     print(f'Jucatori pe teren: {lista_jucatori_teren}')
#     print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#     print(f'Jucatori scosi: {lista_jucatori_scosi}')
# elif x not in lista_jucatori_teren:
#     print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
# elif y not in lista_jucatori_rezerva:
#     print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
# else:
#     print(f'Limita schimbari depasite! {z} schimbari ramase')

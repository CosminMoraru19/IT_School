"""
Recapitulare structuri:

a)structuri de date: liste, seturi, tupluri, dictionare
b) structuri alternative: if-elif-else
c) structuri repetitive: while,


Metode de control al structurilor repetitive:
a) brake-> incheie executia tutoror iteratiilor curenti si viitoare din structura repetitiva
b) continue-> sare peste iteratia curenta, dar exectura iteratiile viitoare:

While este o structura repetitiva care executa un se de instructiuni atata timp cat o conditie este adevarata
    De regula se foloseste atunci cand nu stim exact de cate ori trebuie sa executam setul de isntructiui.
    Cu alte cuvinte se folosseste atunci cand nu stim exact momentul in care conditia nu va mai fi adevarata

    a) o variabila de control al while-ului, de regula declarata inainte de inceperea while-ului(nu e necesara...
    b)inceputul while-ului marcat de cuvantul chele WHILE
    c)conditia de evaluare(cea de baza caruia se va decide daca se mai trece o data prin while sau nu)
    d) separatorul intre conditia de evaluare si corpul while-ului care este caracterul":"
    e) corpul while-ului care este seria de instructiuni care se vor executa

For este o structura repetitiva care executa un se de instructiuni pe baza unui range si care se foloseste
    atunci cand stim exact de cate ori vrem sa repetam un anumit set de instructiuni.
    El se bazeaza pe o variabila de iteratie





"""

# exercitiu 1: Vreau sa printez pe cei 101 dalmatieni:
# variata 1 cu while

# numar_dalmatian = 1
# while numar_dalmatian <= 101:
#     print(f"Dalmatianul curent are numarul {numar_dalmatian}")
#     numar_dalmatian = numar_dalmatian + 1

#varianta 2 cu for
# numar_dalmatian = 1
# for numar_dalmatian in range(numar_dalmatian, 102):
#     print(f"Dalmatianul curent are numarul {numar_dalmatian}")

#exercitiun 2: Vreau sa calculez suma tuturor numerelor de la 1 la 10

# suma = 0
# for i in range(1,11):
#     suma+=i
# print(f'Valoare curenta a sumei este : {suma}')


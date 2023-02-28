# Veriunbea in Romana

from math import pi


# # 1 Clasa Cerc

        # Atribute: raza, culoare
        #
        # Constructor pt ambele atribute
        #
        # Metode:
        # descrie_cerc() - va PRINTA culoarea si raza
        # aria() - va RETURNA aria
        # diametru()
        # circumferinta()

# class Cerc:
#     raza = None
#     culoare = None
#
#     def __init__(self, raza , culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self):
#         print(f' Cercul are culoarea {self.culoare} si raza {self.raza}')
#
#     def aria(self):
#         print(f' Aria cercului definit este {pi * self.raza * self.raza}')
#
#     def diametru(self):
#         print(f' Diametru cercului este {self.raza + self.raza}')
#
#     def circumferinta(self):
#         print(f'Circumferinta cercului este {pi * (self.raza + self.raza)}')
#
#
# cerc1 = Cerc(10, 'Violet')
# cerc1.descriere_cerc()
# cerc1.aria()
# cerc1.diametru()
# cerc1.circumferinta()
# cerc2 = Cerc(220, 'Rosu')
# cerc2.descriere_cerc()
# cerc2.aria()
# cerc2.diametru()
# cerc2.circumferinta()

# # fara cosntructor
# class Cerc:
#     raza = 100
#     culoare = 'alb'
#
#
#     def descriere_cerc(self, raza, culoare):
#         print(f' Cercul are culoarea {culoare} si raza {raza}')
#
#     def aria(self, raza):
#         print(f' Aria cercului definit este {pi * raza * raza}')
#
#     def diametru(self, raza):
#         print(f' Diametru cercului este {raza + raza}')
#
#     def circumferinta(self, raza):
#         print(f'Circumferinta cercului este {pi * (raza + raza)}')
#
#
# cerc1 = Cerc()
# cerc1.descriere_cerc(120, ' alb')
# cerc1.aria(120)
# cerc1.diametru(120)
# cerc1.circumferinta(120)
# cerc2 = Cerc(220, 'Rosu')
# cerc2.descriere_cerc()
# cerc2.aria()
# cerc2.diametru()
# cerc2.circumferinta()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2 -- Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().



# class Dreptunghi:
#     lungime = None
#     latime = None
#     culoare = None
#
#
#
#     def __init__(self, lungime , latime, culoare):
#         self.lungime = lungime
#         self.culoare = culoare
#         self.latime = latime
#
#     def descriere_dreptunghi(self):
#         print(f' Dreptunghiul are culoarea {self.culoare}, latimea de {self.latime} si lungimea de {self.lungime}')
#
#     def aria(self):
#         print(f' Aria dreptunghiului definit este {self.latime * self.lungime}')
#
#     def perimetru(self):
#         print(f' Perimetrul dreptunghiului este {(2 * self.latime) + (2 * self.lungime)}')
#
#     def schimbare_culoare(self, culoare):
#         self.culoare = culoare
#         # print(self.culoare)
#
#
#
# dreptunghi1 = Dreptunghi(2 ,2 , 'alb')
# dreptunghi1.descriere_dreptunghi()
# dreptunghi1.aria()
# dreptunghi1.perimetru()
# dreptunghi1.schimbare_culoare(culoare = 'Visiniu')
# dreptunghi2 = Dreptunghi(4, 5 ,'verde')
# dreptunghi2.descriere_dreptunghi()
# dreptunghi2.aria()
# dreptunghi2.perimetru()
# dreptunghi2.schimbare_culoare(culoare = 'Chrom')
# dreptunghi2.descriere_dreptunghi()



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 3 -- Clasa Angajat

        # Atribute: nume, prenume, salariu
        #
        # Constructor pt toate atributele
        #
        # Metode:
        # descrie()
        # nume_complet()
        # salariu_lunar()
        # salariu_anual()
        # marire_salariu(procent)


# class Angajati:
#     nume = None
#     prenume = None
#     salariu = None
#
#
#
#     def __init__(self, nume , prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descriere(self):
#         print(f'Numele complet al angajatului este  {self.nume} {self.prenume} si are salariu lunar de {self.salariu}')
#
#     def salariu_lunar(self):
#         print(self.salariu)
#
#     def salariu_anual(self):
#         print(self.salariu * 12)
#
#     def marire_salariu(self, procent):
#         self.procent = procent
#         print(f'Salariu a fost marit cu {(self.salariu * procent)/100}')
#
#
#
# angajat1 = Angajati('Moraru', 'Cosmin', 2000)
# angajat1.descriere()
# angajat1.salariu_lunar()
# angajat1.salariu_anual()
# angajat1.marire_salariu(procent = 20)
#
# angajat2 = Angajati('Toader', 'Cristian', 4500)
# angajat2.descriere()
# angajat2.salariu_lunar()
# angajat2.salariu_anual()
# angajat2.marire_salariu(procent = 10)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 4 -- Clasa Cont

    # Atribute: iban, titular_cont, sold
    #
    # Constructor pentru toate
    #
    # Metode:
    # afisare_sold() - Titularul x are in contul y suma de n lei
    # debitare_cont(suma)
    # creditare_cont(suma)



# class Cont:
#     IBAN = None
#     titular_cont = None
#     sold = None
#
#
#
#     def __init__(self, IBAN , titular_cont, sold):
#         self.IBAN = IBAN
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.IBAN} suma de {self.sold} lei')
#
#     def debitare_suma(self, suma_debitata):
#         self.suma_debitata = suma_debitata
#         self.sold = self.sold - self.suma_debitata
#         print(self.sold)
#
#
#     def alimentare_cont(self, suma_alimentata):
#         self.suma_alimentata = suma_alimentata
#         self.sold = self.sold + self.suma_alimentata
#         print(self.sold)
#
# #
# #
# #
# persoana1 =  Cont('IBAN12345', 'Moraru Cosmin', 3000)
# persoana1.debitare_suma(300)
# persoana1.debitare_suma(200)
# persoana1.debitare_suma(1000)
# persoana1.alimentare_cont(1000)
# persoana1.alimentare_cont(1)
# persoana1.afisare_sold()
# print('-------------------------------------------------------')
# persoana2 =  Cont('IBAN1234we24werwe5', 'toader mihai', 50000)
# persoana2.debitare_suma(5235)
# persoana2.debitare_suma(43)
# persoana2.debitare_suma(2)
# persoana2.alimentare_cont(1)
# persoana2.alimentare_cont(1234)
# persoana2.afisare_sold()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 5 -- Clasa Factura
#
        # Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
        #
        # Constructor: toate atributele, fara serie
        #
        # Metode:
        # schimba_cantitatea(cantitate)
        # schimba_pretul(pret)
        # schimba_nume_produs(nume)
        # genereaza_factura() - va printa tabelar daca reusiti
        #
        # Factura seria x numar y
        # Data: generati automat data de azi
        # Produs | cantitate | pret bucata | Total
        # Telefon |      7       |       700       | 49000

#Versiunea 1:

# from datetime import date
# class Factura:
#     seria = 'SNTSITR120020'
#     numar = None
#     nume_produs = None
#     cantitate = None
#     pret_buc = None
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#
#     def schimba_pret(self, pret_nou):
#         self.pret_bucata = pret_nou
#
#     def schimba_nume_produs(self, nume_nou):
#         self.nume_produs = nume_nou
#
#     def genereaza_factura(self):
#         data = date.today()
#         total = self.cantitate * self.pret_buc
#         print(f'Factura seria {self.seria} numarul {self.numar}')
#         print(f'Data {data} ')
#         print(f'Produs |  cantitate | pret bucata | TOTAL ')
#         print(f'{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {total}')
#
# f1 = Factura(12789, 'Telefon', 7, 700)
# f1.genereaza_factura()


#Versiunea 2:

# from datetime import date
# import TableIt
#
#
# class Factura:
#     today = date.today().strftime('%d/%m/%Y')
#     serie = 'ITF 2023'
#
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#         print(f'Cantitatea s-a schimbat in {cantitate}')
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#         print(f'Pretul este acum de {pret} RON')
#
#     def schimba_nume_prodsului(self, nume):
#         self.nume_produs = nume
#         print(f'Noul nume al produsului este {nume}')
#
#     def genereaza_factura(self):
#         factura = Factura
#         print(f'Factura seria: {factura.serie} \nNumar: {self.numar}')
#         print(f'Data: {factura.today}')
#         factura_mea = [
#             ['Produs', 'Cantitate', 'Pret Bucata', 'Total'],
#             [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc],
#         ]
#         TableIt.printTable(factura_mea, useFieldNames=True)
#
#
# factura1 = Factura(1, 'Telefon', 8, 800)
# factura1.schimba_cantitatea(9)
# factura1.schimba_pretul(900)
# factura1.schimba_nume_prodsului('Smartphone')
# factura1.genereaza_factura()
# print('________________________________________________________________________________')
# factura2 = Factura(2, 'Laptop', 10, 2500)
# factura2.schimba_cantitatea(15)
# factura2.schimba_pretul(2000)
# factura2.schimba_nume_prodsului('Laptop Gaming')
# factura2.genereaza_factura()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 6 -- Clasa Masina

        # Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
        # Culoare = gri - toate masinile cand ies din fabrica sunt gri
        # Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
        # Culori disponibile = alegeti voi 5-7 culori
        # Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
        # Inmatriculata = False
        #
        # Constructor: model, viteza_maxima
        #
        # Metode:
        # descrie() (se vor printa toate atributele, inafara de culori_disponibile)
        # inmatriculare() - va schimba atributul inmatriculata in True
        # vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
        # accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
        # franeaza() - masina se va opri si va avea viteza 0

# Versiunea 1:
# class Masina:
#     marca = 'VW'
#     model = None
#     viteza_actuala = 0
#     culoare = 'Gri'
#     inmatriculata = False
#     culori_disponibile = {'alb' , 'rosu' , 'negru' , 'violet' , 'purpuriu'}
#     viteza_maxima = 130
#
#     # def __init__(self, model):
#     #     self.model = model
#
#     def descriere (self, model):
#         print(f'Atia ales masina {self.marca}, modelul {model} care are viteza actuala {self.viteza_actuala},avand culoarea {self.culoare} inmatricularea fiind {self.inmatriculata} ')
#
#     def schimba_inamtric(self, inmatriculata):
#         self.inmatriculata = True
#
#     def vopsea(self, culoare):
#         # for i in range(len(self.culori_disponibile)):
#             if culoare in self.culori_disponibile:
#                 print(f'Masina a fost vopsita in culaorea {culoare} ')
#                 # continue
#             else:
#                 print(f'Culoarea nu este in catalog')
#                 # continue
#     def accelereaza(self, viteza):
#         if viteza < self.viteza_maxima and self.viteza_actuala < self.viteza_maxima:
#             self.viteza_actuala = self.viteza_actuala + viteza
#             print(self.viteza_actuala)
#         elif viteza < 0 :
#             print(f'Viteza este 0. Eroare.')
#
#
#
# masina1 = Masina()
# masina1.descriere('Polo')
# masina1.vopsea('alb')
# masina1.accelereaza(10)
# masina1.accelereaza(20)
# masina1.accelereaza(100)
# masina1.accelereaza(10)

# Versiunea 2:


# class Masina:
#     marca = 'Dacia'
#     viteza_actuala = 0
#     culoare = 'gri'
#     culori_disponibile = {'rosu', 'verde', 'galben', 'albastru', 'mov'}
#     inmatriculare = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(f'Marca masinii este {self.marca}')
#         print(f'Viteza actuala este {self.viteza_actuala}')
#         print(f'Culoarea standard este {self.culoare}')
#         print(f'Este inmatriculata? {self.inmatriculare}')
#
#     def inmatriculare_masina(self):
#         self.inmatriculare = True
#
#     def vopeste_culoarea(self, culoare):
#         self.culoare = culoare
#         if culoare in self.culori_disponibile:
#             self.culoare = culoare
#             print(f'Culoarea a fost inlocuita cu {culoare}')
#         else:
#             print('Culoarea aleasa nu este disponibila')
#
#     def accelereaza(self, viteza):
#         self.viteza = viteza
#         if self.viteza < 0:
#             print('Masina nu poate accelera!')
#         elif self.viteza > self.viteza_maxima:
#             print(f'Masina poate acelera doar pana la {self.viteza_maxima}')
#         else:
#             print(f'Masina accelereaza la {self.viteza} km/h')
#
#     def franeaza(self):
#         self.viteza = 0
#         print(f'Masina s-a oprit iar viteza este acum {self.viteza} km/h')
#
#
# masina1 = Masina('Logan', 200)
# masina1.descrie()
# masina1.inmatriculare_masina()
# masina1.vopeste_culoarea('rosu')
# masina1.accelereaza(150)
# masina1.franeaza()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 7--Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
        # La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
        #
        # Metode:
        # adauga_task(nume, descriere) - se va adauga in dict
        # finalizeaza_task(nume) - se va sterge din dict
        # afiseaza_todo_list() - doar cheile
        # afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
        # daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
        # Daca acesta raspunde nu - la revedere
        # daca raspunde da - il cerem detalii task si salvam nume+detalii in dict

# import json
#
# class ToDoList:
#     todo = {}
#
#     def adauga_task(self, nume, descriere):
#         self.nume = nume
#         self.descriere = descriere
#         self.todo[nume] = descriere
#
#     def afiseaza_todo_list_complet(self):
#         print(json.dumps(self.todo, indent=4))
#
#     def finalizeaza_task(self, nume):
#         self.nume = nume
#         self.todo.pop(nume)
#         print(json.dumps(self.todo, indent=4))
#
#     def afiseaza_todo_list_keys(self):
#         for keys, value in self.todo.items():
#             print(keys)
#
#     def afiseaza_detalii_suplimentare(self, nume_task):
#         self.nume_task = nume_task
#         if nume_task not in self.todo:
#             raspuns = input('Task-ul nu este in lista ToDo, vrei sa il adaugi? \n')
#             if raspuns == 'nu':
#                 print('La revedere')
#             elif raspuns == 'da':
#                 detalii_task = input('Va rugam alegeti o descriere: \n')
#                 self.todo[nume_task] = detalii_task
#                 print(json.dumps(self.todo, indent=4))
#         else:
#             print('Task-ul este deja in lista')


# lista1 = ToDoList()
# lista1.adauga_task('Sa spal vase', 'Cu mult detergent')
# lista1.adauga_task('Sa alerg', 'Repede')
# lista1.afiseaza_todo_list_complet()
# lista1.afiseaza_todo_list_keys()
# lista1.afiseaza_detalii_suplimentare('Fug')
# lista1.finalizeaza_task('Sa spal vase')


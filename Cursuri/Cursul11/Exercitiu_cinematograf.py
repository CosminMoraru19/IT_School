"""
Tema pentru acasa:

Creati o clasa care sa simuleze gestiunea unui cinematograf.

Clasa trebuie sa aiba atribute, metode si constructor explicit (functionalitatea constructorului explicit o veti alege voi)

Va trebui sa definiti metode simple, metode cu parametrii si metode cu parametri si return

Din clasa respectiva veti instantia obiecte si va veti juca cu ele in functie de diverse scenarii pe care vreti sa le faceti (introducere film in gestiune, rulare film, cumparare bilete, rezervare bilete etc)

Daca este posibil definit si functii cu numar nedefinit de parametrii (args / kwargs)
"""
class Cinema:
    def init(self, nume, adresa, capacitate):
        self.nume = nume
        self.adresa = adresa
        self.capacitate = capacitate
        self.filme = []
        self.bilete_vandute = 0
        self.total_incasari = 0

    def add_film(self, film):
        self.filme.append(film)

    def remove_film(self, film):
        self.filme.remove(film)

    def rulare_filme(self):
        print('Filmele ruleaza la', self.nume, 'cinema:')
        for film in self.filme:
            print('-', film.titlu)

class Film(Cinema):

    def init(self, titlu, gen, durata, pret_bilet, locuri_disponibile):
        self.titlu = titlu
        self.genul = gen
        self.durata = durata
        self.pret_bilet = pret_bilet
        self.locuri_disponibile = locuri_disponibile

    def vinde_bilete(self, film):
        if film in self.filme and film.locuri_disponibile > 0:
            film.locuri_disponibile -= 1
            self.bilete_vandute += 1
            self.total_incasari += film.pret_bilet
            print('Bilete in sold pentru', film.titlu)
        else:
            print('Ne pare rau. acest film nu mai ruleaza sau nu mai sunt bilete.')
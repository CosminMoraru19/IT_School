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

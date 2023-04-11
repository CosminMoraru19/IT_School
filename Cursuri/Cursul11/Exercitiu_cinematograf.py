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

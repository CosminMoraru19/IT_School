"""

Encapsularea este o modalitate prin care putem sa ascundem anumite atribute sau metode utilizatorului

Motivul pentru care facem asta este fie din motive de sucuritate sie pentru a morifica modificarea
        anumitor atribute de catre utilizator:
        (ex: peun camp de varsta nu vrem sa permited adaugarea valorilor negative)
Exista 3 tripuri de restrictii:
--public = atributul sau metoda poate fi aceesat oirunde in program
--protected = atributul sau metoda poate fi accesat in afara clasei sau nu este sugerat utilizatorului
--private = atributele sau metoda poate fi accesat si folosit doar in itneriorul clase.

Aceste restrictii vor mai fi identificate in alte limbare de programare (java) cu numele de modificatori de acces.

atributele si metodele public vor fi scrise in mod normal
atributele si metodele protected vor fi precedate de caracterul "_"
atributele si metodele private vor fi precedate  de doua caractere underline "__"



"""

class Casa:
    _nume_etaje = None
    numar_camere = None
    numar_bai = None
    __material_constructie = None
    suprafata = None
    an_constructie = None
    adresa = None
    clasa_energetica = None
    pret = None

    def __init__(self, numar_etaje, numar_camera, numar_bai, material_constructie, suprafata, adresa):
        self.numar_etaje = numar_etaje
        self.numar_camere = numar_camera
        if numar_bai > 2:
            print('Nu putem cosntrui mai mult de doua bai')
        else:
            self.numar_bai = numar_bai
        self.material_constructie = material_constructie
        self.suprafata = suprafata
        self.adresa = adresa

    def calculeaza_aprobare_numar_etaje(self):
        if self.numar_etaje > 5:
            print('Cand unul iti spune ca esti beat mergi mai departe')
        else:
            self.aprobare = True

    def actualizare_an_constructie(self, an_constructie):
        self.an_constructie = an_constructie
        return self.an_constructie

    def vinde_casa(self):
        print(f'Apartamentul de vancare in zona lalelelor'
              f'Numar camere {self.numar_camere}'
              f'Numar etaje {self.numar_etaje}'
              f'Numar bai {self.numar_bai}'
              f'An cosntructie {self.an_constructie}'
              f'Suprafata {self.suprafata}'
              f'Material cosntructie {self.material_constructie}')





















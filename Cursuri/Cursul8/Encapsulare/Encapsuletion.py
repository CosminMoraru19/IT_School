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

ATENTI! In java atributele si merodele priovate pot fi accesate doar in acelasi pachet

Pentru a putea modifica atributele de tip protected, ne folosim de conceptele de getter , settter, deleter

"""

# class Casa_getter_setter_deleter():
#     nume_etaje = None
#     numar_camere = None
#     numar_bai = None
#     __material_constructie = None
#     suprafata = None
#     an_constructie = None
#     adresa = None
#     clasa_energetica = None
#     pret = None
#
#
#     def __init__(self, numar_etaje, numar_camera, numar_bai, material_constructie, suprafata, adresa):
#         self.numar_etaje = numar_etaje
#         self.numar_camere = numar_camera
#         if numar_bai > 2:
#             print('Nu putem cosntrui mai mult de doua bai')
#         else:
#             self.numar_bai = numar_bai
#         self.__material_constructie = material_constructie
#         self.suprafata = suprafata
#         self.adresa = adresa
#
#     def calculeaza_aprobare_numar_etaje(self):
#         if self.numar_etaje > 5:
#             print('Cand unul iti spune ca esti beat mergi mai departe')
#         else:
#             self.aprobare = True
#
#     def __actualizare_an_constructie(self, an_constructie):   #metoda marcata ca fiind privata
#         self.an_constructie = an_constructie
#         return self.an_constructie
#
#     def vinde_casa(self):
#         print(f'Apartamentul de vancare in zona lalelelor'
#               f'Numar camere {self.numar_camere}'
#               f'Numar etaje {self.numar_etaje}'
#               f'Numar bai {self.numar_bai}'
#               f'An cosntructie {self.an_constructie}'
#               f'Suprafata {self.suprafata}'
#               f'Material cosntructie {self.material_constructie}')
#
#     def exemplu_apelrate_metoda(self):
#         return self.__actualizare_an_constructie()
#
#     #getter - o modalitate prin care sa extragem valoarea atributului. Nu trebuie sa aiba alt rol
#
#     def get_materiale_constructie(self):
#         return self.__material_constructie
#
#     # setter - o metoda prin care putem sa modificam valoarea unui atribut. nu trebuie sa aiba alt rol
#
#     def set_materiale_cosntrutie(self,material_cosntructie):
#          self.__material_constructie = material_cosntructie
#
#     # deleter - o modalitate prin care putem sa stergem valoarea unui atribut si nu trebuie sa aiba alt rol
#
#     def delete_materiale_cosntructii(self):
#         self.__material_constructie = None
#
#
# if __name__ == '__main__':
#     garsoniera = Casa_getter_setter_deleter(0 , 1, 1, 'beton', 48, 'Strada lalelelor 23')
#     print(garsoniera.numar_etaje)
#     # print(garsoniera.__materiale_cosntructie) asta nu o sa se vada
#     print(garsoniera.get_materiale_constructie())
#

print('=======================================================')


class Casa_encapsulare_decoratori():
    #decoratorul - modifica comportamentul unei functii
    nume_etaje = None
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
        self.__material_constructie = material_constructie
        self.suprafata = suprafata
        self.adresa = adresa

    def calculeaza_aprobare_numar_etaje(self):
        if self.numar_etaje > 5:
            print('Cand unul iti spune ca esti beat mergi mai departe')
        else:
            self.aprobare = True

    def __actualizare_an_constructie(self, an_constructie):   #metoda marcata ca fiind privata
        self.an_constructie = an_constructie
        return self.an_constructie

    def vinde_casa(self):
        print(f'Apartamentul de vancare in zona lalelelor'
              f'Numar camere {self.numar_camere}'
              f'Numar etaje {self.numar_etaje}'
              f'Numar bai {self.numar_bai}'
              f'An cosntructie {self.an_constructie}'
              f'Suprafata {self.suprafata}'
              f'Material cosntructie {self.__material_constructie}')

    @property
    def materiale_constructie(self):
        return self.__material_constructie

    @materiale_constructie.getter
    def materiale_constructie(self):
        return self.__material_constructie

    @materiale_constructie.setter
    def material_constructie(self, material_cosntructie):
        self.__material_constructie = material_cosntructie

    @materiale_constructie.deleter
    def materiale_constructie(self):
        self.__material_constructie = None

garsoniera = Casa_encapsulare_decoratori(0, 1, 1, 'beton', 48, 'Strada lalelelor 23')
print(f'Materiale de constuctie returnate prin getter inainte  de update{ garsoniera.material_cosntructie}')    #apelare getter
garsoniera.material_cosntructie ='caramida'              #apelare setter
print(f'Materiale de constuctie returnate prin getter dupa update {garsoniera.material_cosntructie}')
del garsoniera.materiale_constructie
print(f'Materiale de constuctie returnate prin getter dupa delete {garsoniera.material_cosntructie}')













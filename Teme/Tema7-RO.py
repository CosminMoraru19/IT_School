# Veriunbea in Romana

# 1
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    Pi = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplemented
    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica,ABC):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self, latura):
        self.__latura = latura

    @latura.getter
    def latura(self):
        print(f'Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print('Am sters latura')
        self.__latura = None

    def aria(self):
        print(f'Aria cercului este : {self.__latura ** 2}')

class Cerc(FormaGeometrica, ABC):


    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Gettar: Raza este : {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter : Noua raza este {raza}')

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am ster latura')
        self.__raza = None

    def aria(self):
        print(f'Aria cercului este : {FormaGeometrica.Pi * (self.__raza ** 2)}')

    def descrie(self):
        print('Eu nu am colturi')

cerc1 = Cerc(10)
cerc1.raza
cerc1.raza = 2
cerc1.aria()
del cerc1.raza
cerc1.raza



patrat1 = Patrat(10)
patrat1.latura
patrat1.latura = 5
patrat1.aria()
del patrat1.latura
patrat1.latura











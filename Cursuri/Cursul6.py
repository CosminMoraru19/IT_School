# def alege_genul():
#     nume = input("Introdu un nume: ")
#     if nume[-1] == "a":
#         print("Numele introdus este de fata.")
#     else:
#         print("Numele introdus este de baiat.")
#
#
# alege_genul()

# Clase/ obiecte/ contructori/ clase importate din alt fisier

# class Car:
#     #atribute/ fields-- caracteristicile pe care le poate avea clasa
#     make = 'Dacia'
#     model = None
#     year = 2023
#     color = 'Alb'
#
#     #metodele -- actiunile pe care le poate face sau sa le suporte clasa noastra
#     def accelerate(self):
#         print('Masina accelereaza')
#
#     def stop(self):
#         print('Masina s-a oprit')
#
#     def chage_color(self, color):
#         self.color = color
#
#
# car1 = Car()
# # car1 este obiect de tip CAr
# print(car1.color)

class Car:
    # fields / attributes - caracteristici pe care le poate avea o clasa
    make = None
    model = None
    year = 2023
    color = None

    def __init__(self, model , color):
        self.model = model
        self.color = color

    # metode - actiuni pe care poate sa le faca sau sa le suporte o clasa
    def accelerate(self):
        print('masina accelereaza')

    # def rezervor(self):
    #     print(f'Rezervorul are o capacitate de {} litri')

    def stop(self):
        print('masina se opreste')

    def change_color(self, color):
        self.color = color

    def model_masina(self, model):
        self.model = model


car1 = Car('Duster', 'albastru')
# car2 = Car()
print(car1.color)3
print(car1.accelerate())
print(car1.stop())
car1.model = 'Duster'
print(car1.model)

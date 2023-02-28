
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 1
# SCHIMBARI_MAX = 3
# x = str(input('Iese de pe teren: \n'))
# y = str(input('Intra pe teren: \n'))
# z = SCHIMBARI_MAX - schimbari_efectuate
#
# if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#     lista_jucatori_teren.remove(x)
#     lista_jucatori_rezerva.remove(y)
#     lista_jucatori_scosi.append(x)
#     lista_jucatori_teren.append(y)
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

lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
lista_jucatori_scosi = []
schimbari_efectuate = 0
SCHIMBARI_MAX = 3
for i in range(1, 4):
    x = str(input('Iese de pe teren: \n'))
    y = str(input('Intra pe teren: \n'))
    schimbari_efectuate +=1
    z = SCHIMBARI_MAX - schimbari_efectuate
    if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
        lista_jucatori_teren.remove(x)
        lista_jucatori_rezerva.remove(y)
        lista_jucatori_scosi.append(x)
        lista_jucatori_teren.append(y)
        print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
        print(f'Jucatori pe teren: {lista_jucatori_teren}')
        print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
        print(f'Jucatori scosi: {lista_jucatori_scosi}')
    elif x not in lista_jucatori_teren:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
    elif y not in lista_jucatori_rezerva:
        print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
    else:
        print(f'Limita de {z} a fost atinsa')
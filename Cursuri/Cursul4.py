#while

# i = 0
#
# while i<6:
#     i += 1
#     if i == 1:
#         continue
#     print(i)


#continue--- reia de la 0 ceea ce se regaseste in conditia forului

# i = 0
# while i<6:
#     i += 1
#     if i == 1:
#         continue
#     print(i)
# Exemplu

# n = input('Type a string: \n')
# list = list(n)
# reverse = list[::-1]
# count = ''
# for i in reverse:
#     count += i
#     if len(count) == len(n):
#         print(count)
#     else:
#         continue



#break-- o sa opreasca iteratia si iese din loop si o orepste

# i = 0
# while i<6:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# Exemplu

# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
# name = input('Nume=')
# for contact in contacts:
#     if name == contact[0]:
#         print(name, "is", contact[1])
#         break
# else:
#     print('Not Found')

#for

# for x in range(100, 6 , -5): #for cu pas (din cat in cat se afiseaza)-- variata descrescatoare/ parcurgere inversa
#     print(x)
#
# for x in range(0, 100 , 5): #for cu pas (din cat in cat se afiseaza)-- varianta crescatoare/ parcurgere directa
#     print(x)

# Exercitii:

#daca vrem sa schimbam una din valorile din lsita de mai sus

# fruits=['apple','banana','cherry']
# for i in range(len(fruits)):
#     if fruits[i]=='banana':
#         fruits[i]='kiwi'
# print(fruits)


#Accelereaza pana nu mai benzina

# benzina=10
# consum=1
#
# while benzina>0:
#     print("Acceleaza")
#     benzina = benzina-consum
#     if benzina<3:
#         print('Alimenteaza')
#         print(f'Mai ai {benzina} litri de benzina')
# else:
#     print("Ai ramas fara benzina")

#Afiseaza doar numerele pozitive dintr-o lista
#
# numere=[-1,2,0,-124,-432,-143,2345,-5435]
# numere_poz=[]
#
# for numar in numere:
#     if numar >= 0:
#         numere_poz.append(numar)
# print(numere_poz)

# for numar in numere:         #afiseaza toate numerele pozitive dintr-un sir de numere
#     if numar<0:
#         continue
#     print(numar)

# for i in range(len(numere)):
#     if numere[i]>0:
#         numere_poz.append(numere[i])
# print(numere_poz)

























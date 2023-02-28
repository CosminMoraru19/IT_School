#Lista

# list1 = ['abc', 30, 'portocala', 'male1', 'male2']
# print(list1)
# print(list1[4])
# print(len(list1))
# print(list1[-1])
# # list1[1] = 'albastru'
# print(list1)
# list1[1:3] = [41, 'lamaie'] # schimbam range de itemi
# print(list1)
#
# list2 = ['mar', 'banana', 'par']
# print(list2)
# list2[1:2] = ['coacaze', 'pepene'] # adauga elemente in functie de indexul specificat si numarul
# de elemente dorite
# print(list2)


#adaugare
# list3 = ['test1', 'test2', 'test3']
# print(list3)
# list3.append('orange') # adauga un singur element la finalul listei
# print(list3)
# list3.insert(0, 'cameleon')
# print(list3)

# scoatere elemente
# list3.remove('test1')  # scoatem elementul dorit aka 'test1'
# print(list3)
# list3.pop(1)  # scoatem elementul cu indexul 1, se pot pune mai multe elemente cu virgula intre
# print(list3)
# list3.pop()  # scoatem ultimul element daca nu se pune valoare la index
# print(list3)
# del list3[1]  # stergem elementul de la indexul specificat
# print(list3)
# del list3  # sterge complet lista
# print(list3)
# print(list3)
# list3.clear()  # goleste lista, ea va ramane, dar nu va avea continut
# print(list3)

# sortare

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# # thislist.sort()
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)

# thislist = [100, 'krer', 50, 65, 82, 23, True, 'asd', 'wre']
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()  # sortare crescatoare
# print(thislist)
# thislist.sort(reverse=True)  # sortare inversa, aka reverse=True
# print(thislist)

# copiere

# thislist = ['apple', 'banana', 'cherry']
# mylist = thislist.copy()
# print(mylist)
# mylist = thislist[:2].copy() # copiaza doar de la indexul de inceput pana la cel specificat
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# concatenare

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# for x in list2:
#     list1.append(x)
#
# print(list1)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3, 4]
# list1.extend(list2)  # = extindem lista 1 cu elmentele din lista 2
# list2.extend(list1)  # = extindem lista 2 cu elementele din lista 1
# print(list1)
# print(list2)
#
# # w3schools.com/python/python_lists.asp


# Dictionar
#
# thisdict = {
#   'brand': 'Ford',
#   'model': 'Mustang',
#   'year': 1964
# }
# print(thisdict)
# print(len(thisdict))
# print(thisdict['brand'])
# x = thisdict.get('model') # accesam cu metoda get + cheia
# print(x)
#
# y = thisdict.keys() # vrem sa aflam care sunt cheile dictionarului
# print(y)


# schimbare valoare

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018 # schimbam anul din 1964 cu 2018
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020}) # schimba valoarea lui year
# print(thisdict)
#
#
# thisdict.update({"anul": 2020}) # adauga o noua cheie: valoare cu anul:2020
# print(thisdict)


# adaugare in dictionar

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red" # adaugam o cheie:valoare la sfarsitul dictionarului
# print(thisdict)

# # scoatere elemente
#
# thisdict = {
#   "brand de brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
}
# thisdict.pop("model") # folosim metoda pop cu numele cheii
# print(thisdict)

# thisdict.popitem() # popitem scoate ultima cheie:valoare din dictionar
# print(thisdict)

# del thisdict["model"] #  dam delete la cheia "model"
# print(thisdict)

# del thisdict # sterge dictionarul cu totul

# copiere

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# thisdict = {
#   "brand1": "Ford",
#   "model2": "Mustang",
#   "year3": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


# nested dictionaries

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
#
# print(myfamily["child1"]["name"])
# print(myfamily["child2"])
# print(myfamily["child3"])

# https://www.w3schools.com/python/python_dictionaries_methods.asp


# Seturi

# thisset = {"apple", 3, "cherry"}
# print(thisset)
#
# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(thisset)

# accesare itemi din set

# thisset = {"apple", "banana", "cherry"}
#
# for x in thisset:
#   print(x)

# verificam daca un anumit item este in set

# thisset = {"apple", "banana", "cherry"}
#
# print("banana" in thisset)

# adaugare element la set

# thisset = {"apple", "banana", "cherry"}
#
# thisset.add("orange")  # metoda add
#
# print(thisset)

# adaugare item dintr-un set in altul
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)

# adaugam elementele unei liste la un set


# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
#
# thisset.update(mylist)
#
# print(thisset)

# scoatere item din set
# thisset = {"apple", "banana", "cherry"}
#
# thisset.remove("banana")
#
# print(thisset)

# # discard la anumiti itemi
# thisset = {"apple", "banana", "cherry"}
#
# thisset.discard("banana")
#
# print(thisset)


# scoatem un item random

# thisset = {"apple", "banana", "cherry"}
#
# x = thisset.pop()
#
# print(x)
#
# print(thisset)

# golim setul

# thisset = {"apple", "banana", "cherry"}
#
# thisset.clear()
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
#
# del thisset
#
# print(thisset)

# unim doua seturi
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2) # creeaza un nou set cu itemele din cele 2 seturi
# print(set3)

# metoda update

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set1.update(set2) # updateaza setul 1 cu itemele din setul 2
# print(set1)

# union si update vor exclude orice duplicate daca exista



# Tuple - are elemente imutabile

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
#
# print(thistuple[1])
#
# # workaround pentru a schimba valorile unei tuple
#
# x = ("apple", "banana", "cherry") # tupla
# y = list(x) # convertim din tupla in lista
# y[1] = "kiwi" # schimbam elementul de la indexul dorit
# x = tuple(y) # convertim inapoi in tupla
#
# print(x)

# pentru a adauga items trebuie conversie

# thistuple = ("apple", "banana", "cherry") # tupla initiala
# y = list(thistuple) # convertire la lista
# y.append("orange") # append pentru a adauga la lista un element la final
# thistuple = tuple(y) # convertire la tupla
# print(thistuple)


# update tuple

# thistuple = ("apple", "test", "cherry")
# y = ("orange",)
# thistuple += y  # la fel ca thistuple = thistuple + y
#
# print(thistuple)


# unpacking la tupla

# fruits = ("apple", "banana", "cherry")
#
# (green, yellow, red) = fruits
#
# print(green)
# print(yellow)
# print(red)



# numarul variabilelor trebuie sa faca match la numarul valorilor din tupla

# unire 2 tuple

# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)
#
# tuple3 = tuple1 + tuple2
# print(tuple3)

# multiplicare
#
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
#
# print(mytuple)

# lungimea unei tuple
#
# fruits = ("apple", "banana", "cherry")
# print(len(fruits))


# metode tuple
# https://www.w3schools.com/python/python_tuples_methods.asp


# list1 = [1, [2, 3], 2, 4]  # lista in lista
# print(list1[1])
# print(type(list1[1]))
# print(type(list1[0]))


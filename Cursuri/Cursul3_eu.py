#Structuri de date/ coelctii de date.

#ce mai folosita structura de date este lista
# tipuri: Lista -- se pot scrie duplicate
# Dictionar--
# set
# Truplu

# Lista- Pastreaza mai multe valori intr-o singura variabila
#
# list1= ['abc', 34, 'portocala', 2345, 'agg', 'agg']
# print(list1)
# print(list1[0])
# print(len(list1))
# print(list1[-3])
# list1[1]= 'albastru'
# print(list1)
# list1[1:3]=[1245,'lalal',False]   #ultima pozitie(3 in cazul de fata) se pastreaza in sir.(int-o pozitie anume)
# print(list1)

# list2= ['mar','banana','Cireasa']
# print(list2)
# list2[1:2]=['coacaze','pepene',141325,12352435,1431324]
# print(list2)

#adaugare ceva in sir-- la sfarsit
# list1.append('orange')
# print(list1)
# list1.insert(4, 'cameleon') # adaugare pe o anumita pozitie
# print(list1)
# list1.remove('abc')   #scoate un element din sir, dar trebie scris exact elementul
# print(list1)
# list1.pop()  # scoate ultimul element din sir si daca punem indexul, scoate indexul respectiv (1,2,3,4)
# print(list1)
# del list1[1]  # sterge elementul de la indexul specificat.
# print(list1)
# del list1     #sterge intreaga lista.
# print(list1)
# list1.clear()    #se goleaste lista cu totul
# print(list1)

#sortare

# thislist=['orange','mango','kiwi','pineapple','banana']
# thislist.sort()      #sorteaza in ordine alfabetica --- nu merge sa amesteci tipurile de variabile --sortarea crescatoare
# print(thislist)
# thislist.sort(reverse=True)   #sortare inversa
# print(thislist)
# myList=thislist.copy()    # copiaza toata lista
# print(myList)
# myList=thislist[:1].copy()   #copiaza intr-un amnumit range de indexuri
# print(myList)
#
# thisList= ['apple','banana','cherry']
# mylist = list(thisList)
# print(mylist)
#
# list1=['a','b','c']
# list2=[1,2,3,4]
# ListaConcatenate= list1+list2     #concatenare clasica
# print(ListaConcatenate)


# list1=['a','b','c']
# list2=[1,2,3,4]
# list1.extend(list2[:4])     #concatenare cu doar cate va indexuri
# list2.extend(list1)         #extinder lista 2 cu elementele din lsita 1
# print(list1)
# print(list2)

# de cautat despre lista          w3schools.com/python/python_lists.asp

# Dictionare!!!

# thisdict={
#     'brand':'Ford',
#     'model':'Mustang',
#     'year': 1964
# }
# print(thisdict)
# print(len(thisdict))
# print(thisdict['brand'])
# x=thisdict.get('model')     # accesam cu metoda get + cheie
# print(x)
#
# y=thisdict.keys()   # comanda care ne arata toate cheile din dictionar
# print(y)

#schimbarea valorilor dintr-un dictionar

# thisdict={
#     'brand':'Ford',
#     'model':'Mustang',
#     'year': 1964
# }
# thisdict['year']=2018    #se schimba anul din 1964 in 2018
# print(thisdict)

# #adaugarea unei noi chei
# thisdict={
#     'brand':'Ford',
#     'model':'Mustang',
#     'year': 1964
# }
# thisdict.update({'year':2020})   # schimba valoea lui year
# print(thisdict)
# thisdict.update({'anul':2020})   # adauga o noua cheie.
# print(thisdict)

#adaugarea in dictionar a itemelor
# thisdict={
#     'brand':'Ford',
#     'model':'Mustang',
#     'year': 1964
# }
# thisdict['color']='red'     #adaugam o noua cheie:valoare la sfarsitjul dictionarului
#
# print(thisdict)

# scoaterea unor chei
# thisdict={
#     'brand':'Ford',
#     'model':'Mustang',
#     'year': 1964
# }
# thisdict.pop('model')     #folosim metoda pop cu numele cheii
# print(thisdict)

# thisdict.popitem()    # scoate ultima cheie:valoare din dictionar
# print(thisdict)

# del thisdict['model']     #stergem cheia 'model'
# print(thisdict)

# del thisdict                # se sterge dictioanrulu cu totul

# mydict= thisdict.copy()
# print(mydict)

# thisdict={
#     'brand':'Ford',
#     'model2':'Mustang',
#     'year3': 1964
# }
# mydict= dict

#de pus aici dictionarul in dictionar

#https://www.w3schools.com/python/python_dictionaries_methods.asp
# #Seturi
# thisset={'apple',3, 'cherry'}
# # print(thisset)
#
# for x in thisset:               #afisaza ce e in seturi
#     print(x)

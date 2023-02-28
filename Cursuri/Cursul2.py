# Operatori
#
# de atribuire

# x = 3
# print(x)
# x+=3 #x=x+3
# print(x)
# x-=3 #x=x-3
# print(x)
# x*=3 #x=x*3
# print(x)
# x/=3 #x=x/3
# print(x)

#aritmetici

# x= int(input('Introdu x:'))
# y= int(input('Introdu y:'))
# z=x+y
# n=x-y
# p=x*y
# i=x/y
# k=x%y # Modulo-- restul impartirii
# v=x**y #ridicare la putere pe primul la al doilea
# print(z,n,p,i,k,v)
#
# #comparare
# a = 5
# b = 5
# assert a==b
# assert a!=b   #diferite
# assert a>b
# assert a<b
# assert a<=b

#operatori logici

# and -- returneaza true daca ambele conditii sunt adevarate
#or- returneaza true daca cel putin una dintre conditii este adevarata
# not -- returneaza false daca rezultatul este adevarat, adica fals
#not(x<5 and x<10)

# x= 5
# y=6
# z=11
# # assert x == 5 and y==6
# # print('assert ok')
# # assert not(x==7)

a = 3
b = 5
# if not a==3:   # se neaga  argumentul
#     print(' A nu este 3')
# else:
#     print('A este 3')
# if a== 3:     # nu se neaga agumentul- afirmatia inatiaiala este adevarata
#     print('A este 3')
# else:
#     print('A nu este 3')

if not(type(a) == int):
    print('tipul lui a  este int')
else:
    print('tipul lui a nu este int')


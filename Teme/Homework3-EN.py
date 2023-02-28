# Versiune limba romana


# 1. -- Declare a list of musical_notes in which to put do re mi etc until do
#     a. Display it
#     b. Reverse the order using slicing and overwrite this list, then print current version (inverted)
#     c. On this list, apply a method that you suspect does the same thing, that is to say
#     reverse the order (You don't need to override it in this case, because the method does
#     this automatically) and then prints the current version of the list. You're basically back to he original version
# Conclusions: slicing is temporary, if you want to keep the new version you have to
#     overwrite the list or save it in a new list. The method you found does
#   automatically overwriting and making these changes permanent.  Both variants have their the utility depending on what we want at that moment.


from typing import List

# note = ['do', 're', 'mi', 'fa','sol','la','si','do']
# print(note)    #a
# note = note[::-1]   #b
# print(note)
# note.reverse()  #c
# print(note)     #d


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2 -- Shows on the screen how many times the note 'do' appears in the list.
# note = ['do', 're', 'mi', 'fa','sol','la','si','do']
# do = note.count('do')
# print(do)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#3 -- Having 2 lists, [3, 1, 0, 2] and [6, 5, 4], find 2 options to join them in a single list.

# list1 = [3,1,0,2]
# list2 = [6,5,4]
# full_list = list1+list2
# print(full_list)
# list1.extend(list2)
# print(list1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#4-- Sort and display the list generated in the previous exercise. Delete number 0 from the list
#           using a function and then display the list again

#
# full_list.sort()
# print(full_list)
# del full_list[0]
# print(full_list)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 5 -- Using an if, check the list generated in exercise 3 and display the following on each branch:
#       - The list is empty (IF):
#       -The list is not empty (ELSE)


# if len(full_list) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#6 -- Use a function to empty the list from exercise 3

#
# full_list.clear()
# print(full_list)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 7-- Rewrite the if from exercise 5 and check the result once more. Now it should be displayed that the list is empty


# if len(full_list) == 0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 8 -- Having the dictionary dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, use a function to display the Students (keys)


# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# print(dict1.keys())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 9--  Print the 3 students from the above dictionary and their grades respectively
#       Ex: 'Ana got the grade {x}'.
#       You will only take the note using the key


# x = dict1.get('Ana')
# print(f'Ana took the grade {x}')
# y = dict1.get('Gigel')
# print(f'Gigel took the grade {y}')
# z = dict1.get('Dorel')
# print(f'Dorel took the grade {z}')




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#10 -- Imagine that Dorel filed an appeal and received a grade 6.
# - Change Dorel's note in 6
# - Print his note after modification


# dict1['Dorel'] = 6
# print(dict1)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 11 -- Imagine that Gigel transfers from the class.
    # - Look for a function to delete it
    # A new colleague is coming.
    # - Add Ionica to the list, with grade 9
    # - Print the dictionary with the new students

#del dict1['Gigel']
# print(dict1)
# dict1.update({'Ionica':9})
# print(dict1)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 12-- You have the following sets:
    # week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
    # weekend = {'saturday', 'sunday'}
    # - Try adding 'Monday' to the set of weekd_days "Monday" and see what happens.
    # -Display the week_day set and see the result of the previous addition.


#
# week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
# weekend = {'saturday', 'sunday'}
# week_days.add('Monday')
# print(week_days)    #nothing happens because we cannot have duplicates in sets



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#13 --Use an if and check if:
    # - Weekend is a subset of the days of the week (that is, if the elements in the weekend set
    # find among the elements in the week_day set
    # - Weekend is not a subset of the days of the week
    # Hint: You can use either the comparison operator or a function. The result of each
    # point above will be a boolean


# if weekend.issubset(week_days):
#     print('Weekend este subset al zilelor saptamanii')     #maybe not right
# else:
#     print('Weekend nu este subset al zilelor saptamanii')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#14 -- It shows the differences between these 2 sets (that is, the elements that are in week_days and are not in weekends and vice versa)

#
# difset = week_days-weekend
# print(f'the difference between the two sets is{difset}')
# diferenta = week_days.difference(weekend)
# print(diferenta)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





# 15 -- It displays the intersection of the elements from these 2 sets (that is, the elements that exist in both sets). Hint: You can use a function


# common_elements = weekend.intersection(week_days)
# print(common_elements)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#Optional exercises

# 1 --   We imagine a football team during the match. A maximum of 3 changes are allowed.
    # - Declare a list with 5 players: list_jucatori_teren
    # - Declare a list of 5 reserve players: list_jucatori_reserva
    # -Declare an empty list of players sent off: list players sent off
    # - Changes Made = play with different values to see how the data passes through the code
    # - CHANGE_MAX will be a constant with the value 3
    # If Player x is on the field and we still have changes available then:
    # - We make the change if the player is in the reserve list and does not exist in the players on
#    land
    # - We delete the removed player from the field list and add him to the removed players list
    # - We add the entered player to the list of players on the field and remove him from the list of players
#    reserve
    # -I displayed on the screen: x entered, y exited. You have z more changes (replace x, y and z with the name
#    of your variables
    # If the player we want to change is not on the field:
    # -Display 'the change cannot be made because player x is not on the field'
    # Otherwise, display the screen: 'you still have z changes'




# First version
# lista_jucatoru_teren = ['Cosmin','Mihai','Marian','Alberto','Paul']
# lista_jucatori_rezerva = ['Roberto','Costel','Dorin','Doru','Daniel']
# lista_jucatori_scosi = []
# Schimbari_maxim = 3
# Schimbari_efectuate = 0
#
# for x in lista_jucatori_rezerva:
#     if x in lista_jucatoru_teren or Schimbari_maxim >= 1:
#         lista_jucatori_scosi.insert(0,lista_jucatori_teren.remove(0))
#         print(f'A iesit jucatorul {lista_jucatoru_teren.pop(0)}')
#         print(f'A iesit jucatorul {lista_jucatori_scosi(0)}')
#         print(f' mai aveti {Schimbari_maxim = Schimbari_maxim-1}')
#         print(f'S-au efectuat {Schimbari_efectuate=Schimbari_efectuate+1) schimbari)
#     else:
#         print(f'Scimbarea nu se paote efectua')

# second version
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 1
# SCHIMBARI_MAX = 3
# x = str(input('Iese de pe teren: \n'))
# y = str(input('Intra pe teren: \n'))
# z = SCHIMBARI_MAX - schimbari_efectuate
#
# # for x in lista_jucatori_teren or y in lista_jucatori_rezerva:
# if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#     lista_jucatori_teren.remove(x)
#     lista_jucatori_rezerva.remove(y)
#     lista_jucatori_scosi.append(x)
#     lista_jucatori_teren.append(y)
#
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

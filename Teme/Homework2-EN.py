#English version.

#1 -- Explain in your own words in a comment how an if else works

# The If function is a function that can return 2 or more different results, depending on a preset condition.
# If the argument is true, it will generate the desired result, if the argument is false, then it will skip the action.



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 2--Checks and displays if x is a natural number or not (a number is considered natural if it is an integer greater than 0)


# x = 'safdf'
# if type(x) == int and x>0:
#     print(f'The number {x} is an integer')
# else:
#     print(f'The number {x} is not integer')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#3--- Checks and displays if x is a positive, negative or neutral number


# x= int(input('Number:'))
# if x > 0:
#     print(f'{x} is positive')
# elif x < 0:
#     print(f'{x} is negative')
# else:
#     print(f'{x} is neutral')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#4-- Checks and displays if x is between -2 and 13 (including interval ends).


# x = int(input('Number:'))
# if x > -2 and x < 13:
#     print(f'{x} it is in the interval')
# else:
#     print(f'{x} it is not in the interval')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#5-- Checks and displays if the difference between x and y is less than 5 (the difference means
#              how many numbers are between x and y, not the result of the difference between x and y).


# x = int(input('x='))
# y = int(input('y='))
# if x-y < 5:
#     print(f'The difference between the numbers is less than 5')
# else:
#     print(f'The difference between the numbers is not less than 5')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#6-- Checks if x is NOT between 5 and 27, including interval ends. (to use 'not')

#
# x = int(input('x='))
# if not( x>= 5 and x <= 27):
#     print(f' {x} is not in the range')
# else:
#     print(f' {x}  is in the range')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#7 -- Declare a new variable y of type int and then check and display if x and y are equal,
#        if not, display which one is bigger



# x = int(input('x ='))
# y = int(input('y ='))
# if x == y:
#     print(f'The numbers are equal')
# elif x > y:
#     print(f'x is the bigger number')
# else:
#     print(f'y is bigger')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#8 -- Assuming that x, y, z (all of type int) - represent the sides of a triangle, display if
#           the triangle is isosceles (two sides are equal), equilateral (all sides are equal) or
#               any (no side is equal).


# x= int(input('x='))
# y= int(input('y='))
# z= int(input('z='))
# if x == y == z:
#     print(f'The triangle with sides x,y,z is isosceles')
# elif (x==y or y==z or x==z) and (x!=z or x!=y or y!=z or y!=x or z!=x or z!=y):
#     print(f'The triangle with sides x,y,z is equilateral')
# else:
#     print(f'The triangle with side x,y,z is certain')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#9-- It reads a letter from the keyboard, then checks and displays whether it is a vowel or not.
#       Careful!    You must evaluate both uppercase and lowercase cases.



# x = input('Litera=')
# if x == 'a' or x == 'A':
#     print(f'{x} is vocal')
# elif x == 'e' or x == 'E':
#     print(f'{x} is vocal')
# elif x == 'o' or x == "O":
#     print(f'{x} is vocal')
# elif x == 'i' or x == 'Y':
#     print(f'{x} is vocal')
# elif x == 'u'or x == 'U':
#     print(f'{x} is vocal')
# else:
#     print(f'{x} is not vocal')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#10 -- Convert and print notes from the Romanian system to the American system as follows:
                # a. above 9 => A
                # b. above 8 => B
                # c. above 7 => C
                # d. above 6 => D
                # e. above 4 => E
                # f. 4 or under => F



# x=int(input('Grade='))
# if x >= 9:
#     print(f'Grade A')
# elif x >= 8 and x < 9:
#     print(f'Grade B')
# elif x >= 7 and x < 8:
#     print(f'Grade C')
# elif x >= 6 and x < 7:
#     print(f'Grade D')
# elif x >= 4 and x < 6:
#     print(f'Grade E')
# elif x < 4:
#     print(f'Grade F')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# Optional exercises:

#1 --  Check if x has at least 4 digits (eg: 7895 has 4 digits, 10 does not have at least 4 digits)


# x = 12
# if x.bit_count() >= 4:
#     print(f'{x} has at least 4 digits')
# else:
#     print(f'{x} does not have at least 4 digits')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# 2 -- Check if x has exactly 6 digits


# x = 123456
# if x.bit_count() == 6:
#     print(f'{x} has 6 digits')
# else:
#     print(f'{x} does not have 6 digits')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#3 -- Check if x is an even or odd number

# x = 12343
# if  x%2 == 0:
#     print(f'{x} it is even')
# else:
#     print(f'{x} is odd')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#4 -- Having three variables x, y, z (all int) displays in the console which is the largest of them


# x= int(input('x='))
# y= int(input('y='))
# z= int(input('z='))
#
# if x > y and x > z:
#     print(f'x is the largest number')
# elif y > x and y > z:
#     print(f'y is the largest number')
# else:
#     print(f'z is the largest number')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 5 -- Assuming that x, y, z - represent the angles of a triangle, check and display if
    # is the triangle valid or not (a triangle is valid if the sum of all angles is
    # 180 degrees or if the sum of the lengths of any two sides is greater than
    # length of the third side)


# AB= int(input('AB='))
# BC= int(input('BC='))
# AC= int(input('AC='))
#
# if AB + BC + AC == 180 and AB > 0 and BC > 0 and AC > 0:
#     print(f'The triangle formed by the sides AB, AC and BC is valid')
# else:
#     print(f'The triangle formed by the sides AB, AC and BC is not valid')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#6 --  Having the string: 'Coral is either the stupidest animal or the smartest rock' read by
    # to the keyboard an int number x and displays the string without the last x characters. eg: if
    # you chose 7, the following string will be displayed: 'Coral is either the stupidest animal or the
    # smarte'


# String='Coral is either the stupidest animal or the smartest rock'
# x = int(input('x ='))
# print(String[0:-x])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




# 7-- Using the same string from exercise 6, declare a new string consisting of the first 5 characters + the last 5

#
# String = str('Coral is either the stupidest animal or the smartest rock')
# First_part_string = String[0:5]
# Lenght_string_wtihyou_last_5 = len(String)-5
# Last_part_string = String[Lenght_string_wtihyou_last_5:]
# print(Last_part_string)
# New_String=First_part_string+' acesta este un si nou ' + Last_part_string
# print(New_String)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#8 -- Using the same string from exercise 6, save to a variable and display
# the start index of the word rock - i.e. the position in the string at which the word rock begins
# (hint: there is a function that helps you do this). Using this variable + slicing,
# display the entire string up to this word. Expected output: 'Coral is either the stupidest
# animal or the smartest '

# x = 'Coral is either the stupidest animal or the smartest rock'
# y = len(x) - 4
# z = x[y:]
# print(x[:y])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#9 -- Read a string from the keyboard and check if the first and last characters are the same.
# An assert will be used. Attention: we want the program to be case insensitive, means 'apA'
# is accepted as a string in which the first and last character are the same (hint, you can use o
# function to make the string case insensitive)


# x = input('Write a word: ').upper()
# assert x[0] == x[-1]
# print('correct')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 10-- Having the string '0123456789' displays only the even numbers and then only the odd numbers
# (hint: use slicing and control the display in slicing with slicing step)

# x = '0123456789'
# print(x[2::2], x[1::2])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercitii bonus!

#1--  We want to create an application for purchasing plane tickets that will receive justice
# input the following information:
        # a. Age
        # b. Accompanied by my mother
        # c. Accompanied by father
        # d. Passport
        # e. Permission act mother
        # f. Permission act father
# Boarding conditions:
        # 1. If the person is over 18 years old and has a passport
        # 2. If the person is under 18, has a passport and is accompanied by both parents
        # 3. If the person is under 18 years old, which passport, he is accompanied by at least one parent
        # and has written permission from the other parent
#
# Write the code that implements the boarding conditions above and test it with everything
# the variants you think should be tested. Generate test scenarios with expected results and
# then run the code to check if expected results are equal to actual results.
# Examples:
    # 1. Age 19, I don't have a passport => I can't board
    # 2. Age 17, I have a passport, both parents => I can board



# a = int(input('Varsta: '))
# b = input('Accompanied by the mother? (Yes/No) ')
# c = input('Accompanied by father? (Yes/No) ')
# d = input('Passport (yes/no) ')
# e = input('Permission slip mom? (Yes No) ')
# f = input('Permission slip dad? (Yes No) ')
# if a >= 18 and d == 'yes':
#     print(f'Age {a} years, I have a passport => I can board')
# elif a < 18 and d == 'yes' and c == 'yes' and b == 'yes':
#     print(f'Age {a} years, I have a passport, both parents, no permission documents => I can board')
# elif a < 18 and d == 'yes' and (b == 'yes' and f == 'yes') or (c == 'yes' and e == 'yes'):
#     print(f'Age {a} years, I have a passport, at least one parent and the permission document of the other => I can board')
# else:
#     print('I can't board either because I don't have a passport, a parent or a permission slip if I'm a minor')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 2-- Gamble game

# Search the net and see how a random number is generated
# - Imagine that you roll the dice and save this number in a variable called dice_roll.
# The saved number will be randomly generated using the method found online
# - Enter a number from the keyboard to represent the number chosen by the user
# - Checks and displays if the user has guessed the number
# - There will be 3 options that will have to be dealt with:
# ● You lost. You chose a smaller number. You chose x but it was y
# ● You lost. You chose a higher number. You chose x but it was y
# ● You guessed it. Congratulations? You chose x and the die was y

# import random
# dice_roll = (random.randint(1, 6))
# x = int(input('Choose a number: '))
# if x == dice_roll:
#     print(f'You guessed it! Congratulations! You chose {x} and the dice was {dice_roll}')
# elif x > dice_roll:
#     print(f'You lose. You chose a higher number. You chose {x} but it was {dice_roll}')
# else:
#     print(f'You lose. You chose a smaller number. You chose {x} but it was {dice_roll}')
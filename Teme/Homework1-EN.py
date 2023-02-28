# English language version.
# 1 -- In a comment, explain in your own words what a variable is.

# A variable is a value preset by the user and memorized by the computer to use it every time it is accessed.


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # 2 --- Declare and set one variable of each of the following variable types:

# Name = 'Cosmin'
# Age = 26
# Grade = 8.32
# Passed = True

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # 3 -- Use the type function to check if they have the expected data type.

# print(type(Name))
# print(type(Age))
# print(type(Grade))
# # print(type(Passed))


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #  4 -- Round the float using the round() function and save this change in the same variable (override):
#               - Check it's type

# print(round(Grade))
# print(type(round(Grade)))
# Grade=round(Grade)
# print(Grade)
# print(type(round(Grade)))



# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #5 -- Use print() and print 4 statements to the console using the 4 variables.

# print('My age is '+ str(Age))
# print(f'I've finished the highschool with grade {Grade}')
# print(f'My name is {Name}, i am  {Age} old, my grade is {Grade} and i am  {Passed}')


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #6 -- Read from the keyboard:
#               - Last Name;
#               - First Name
#              Display: 'Full name has x characters'.


# last_name = input('Last Name: ')
# first_name = input('First Name:')
# print(f'Full name has  {len(last_name)+len(first_name)} characters')



# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 7 -- Read from the keyboard:
#       - lenght;
#       - width.
#         Display: 'The area of the rectangle is x'

# lenght = int(input('Lenght: '))
# width = int(input('Width: '))
# print(f'The area of the ragtangle is {lenght * width}')


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #8 -- Having the string: 'Coral is either the stupidest animal or the smartest rock':
#              - display the number of occurrences of the word 'the';


# string = 'Coral is either the stupidest animal or the smartest rock'
# print(string.count(' the '))


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 9 --Same string.
#            replace 'the' with 'THE'
#            print the result

 # string = 'Coral is either the stupidest animal or the smartest rock'
 # print(string.replace(' the ', ' THE '))


# Optional exercises.

# 1 -- Read an odd-sized string from the keyboard;
#        - display the middle character.

#First version:

# name = input('Name')
# print(f'The middle character is  {name[(len(Name)//2)]}')

# second version:

# input_string = str(input('Insert string with odd character length: '))
# length_string = len(input_string)
# if length_string % 2 != 0:
#     divide_string = length_string // 2
#     print('The middle character is:', input_string[divide_string])
# else:
#     print('Only strings with odd character length are accepted! Rerun script!')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#2 -- Using assert, check if a string is a palindrome.

# word = input('insert word:')
# word_backwords = str(word[::-1])
# assert word == word_backwords
# print("the word is palindrome")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 3 -- Exercise:
#           - reads a string from the keyboard (ex: alabala orange);
#           - save the first character in a variable - whatever it is, try 2 different strings;
#           - capitalize this character everywhere except for the first and last characters => alAbAlA portocAla.


# string = input("String:")
# Variable = string[0]
# # print(Variable)
# Upp_letter = Variable.upper()
# # print(Upp_letter)
# string_majuscule = string.replace(string[0], Upp_letter)
# print(string_majuscule)
# Variable_majuscula = string_majuscule[0]
# low_letter = Variable_majuscula.lower()
# # print(low_letter)
# Final=string_majuscule.replace(string_majuscule[0],low_letter)
# print(Final)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 4-- Exercise:
#       - read a user from the keyboard;
#       - read a password;
#        - display: 'Password for user x is ***** and has x characters';
#        - ***** will be dynamically calculated regardless of password size, it must display correctly.


# User= input("User:")
# Password = input("Passwor:")
# Lenght_Password=len(Password)
# print(f'Password of User {User} is {Lenght_Password * "*"} adn has {len(Password)} characters')

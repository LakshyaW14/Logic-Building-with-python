# while True:

#     x =int(input("Enter the number : "))

#     y = "yes" if ((x % 3) == 0 and (x % 5) == 0) else "no"
#     print(y)
    

# char = input("Enter the character :")
# vowels ="aeiou"
# # for char in vowels :
# if char in vowels:
#     print ("Is vowel")
# else:
#     print("Is Consonant")

# while True:
#     ch = input("Enter your character :")
#     if len(ch) != 1:
#         print("Enter only one character")
#         continue

#     if ch.isupper():
#         print ("Character is uppercase ")
    
#     elif ch.islower():
#         print ("Character is lowercase ")

#     elif ch.isdigit():
#         print ("charcter is a digit ")

#     else :
#         print ("ch is a special character ")


# while True:

#     S1 = int(input("Enter the side 1 "))
#     S2 = int(input ("Enter the side 2 "))
#     S3 = int(input ("Enter thr side 3 "))

#     if (S1 <= 0) or  (S2 <= 0) or (S3 <= 0):
#         print ("invalid side , must be positive")
        

#     if ( S1 + S2 > S3) and ( S1 + S3 > S2) and ( S2 + S3 > S1):
#         print ("Valid sides to form a triangle ")

#         if ( S1 == S2 == S2 == S3):
#             print("The triangle is an equilateral triangle ")
#         elif (S1 == S2 or S1 == S3 or S2 == S3):
#             print("the triangle is an isoceles triangle")
#         else:
#             print("The triangle is a scalene triangle ")


#     else :
#         print ("Invalid sides to form a triangle" )



# question 3

# num1 = 12
# num2 = 4 
# if num1 == 0 or num2 == 0 :
#     print( "Cannot check multiple with zero")

# if num1 % num2 == 0:
#     print ("Number 1 is a multiple of number 2 ")
# elif num2 % num1 == 0:
#     print ("Number 2 is a multiple of number 1 ")
# else:
#     print (" neither number is a multiple of other number ")

# questions 4 

# while True:
#     hour = int(input( "Enter the hour of the day [0-23] :"))
#     if hour > 24 :
#         print("Invalid hour time ")
#     elif 0 < hour < 12 or hour == 24 :
#         print("Good Morning !")
#     elif 12 < hour < 17 :
#         print ("Good Afternoon !")
#     elif 17 < hour < 21:
#         print ( "Good Evening !")
#     else :
#         print ("Good Night !")


# question 5 

# while True:
#     age = int(input ("Enter the age of the voter :"))
#     if age < 0 :
#         print("Invalid age")
#     elif age < 18  :
#         print ("Not eligible to vote, [Minor]")

#     else:
#         print ("Eligible, can vote")


# question 6 

# num1 = int(input("Enter first number :"))
# num2 = int (input("Enter second number:"))
# if num1 % 2 == 0 and num2 % 2 ==0:
#     print ("both numbers are even")
    
# else :        

#     if num1 % 2 == 0 :
#         print("num1 is even" )
#     else:
#         print("Num1 is odd")

#     if num2 % 2 == 0 :
#         print("num2 is even" )
#     else:
#         print("Num2 is odd")

    
#question 7 

# ch = input("Enter the character :")

# if len(ch) != 1 or not ch.isalpha():
#     print("please enter a single alphabat")

# elif 'a' <= ch <= 'm':
#     print("The character lies between a to m ")
# else:
#     print("the character lies between n to z ")


# question 8 
# day = int (input ("Enter the number of the day :"))

# match day:
#     case 1:
#         print("Monday")
#     case 2 :
#         print("Tuesday")
#     case 3 :
#         print("Wednesday")
#     case 4 :
#         print("Thursday")
#     case 5 :
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid number")

#question 10
while True:
    marks = int (input ("Enter your marks :"))

    if marks < 0 or marks >100 :
        print ("invalid marks ")
    elif 90 < marks < 100:
        print("Grade A")
    elif 80 < marks < 90 :
        print("Grade B")
    elif 60 < marks < 80 :
        print ( "Grade C")
    elif 33 < marks < 60 :
        print ("Grade D")
    else:
        print("Grade F")



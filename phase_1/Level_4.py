# Question 1

ch = input("enter your character ")

if  ch.isalpha():  
    print("is a letter")
elif  ch.digit():
    print ("is a number ")
else:
    print("Neither")

# other method

ch_lower = ch.lower()
if ( 'a' <= ch_lower <= 'z'):
    print("is a letter ")
elif  ( '0' <= ch <= '9') or ch < '0':
    print("is a digit")
else:
    print("Is neither ")

# Question 2 


num = int (input("Enter the number "))

if ((num % 3)==0 and (num % 5)==0):
    print("fizzbuzz")
elif ( num % 5 ) == 0 :
    print ("Buzz")
elif (num % 3)==0 :
    print("fizz")
else:
    print("not divisible ")

# question 3

x,y,z = map(int, input("Enter three numbers :").split())

mean = (x + y + z)/3
if (x > y and x < z ) or ( x< y  and x>z):
    print (f"{x} is a median value ") 
elif ( y > x and y < z ) or ( y < x and y > z ):
    print (f"{y} is a median value ")
elif (z > x and z < y ) or ( z < x and z > y):
    print (f"{z} is a median value ")
else:
    print("invalid value ")


# Question 5 


income, age = map (int, input ("Enter the income ( in lakh ) and age ( in years) :").split())

if ( income > 5) and ( age > 18):
    print("Eligible for tax ")
else :
    print("Not eligible ")

# Question  6 

x,y = map(int, input ("Enter two numbers :").split())
if ( x> 0) and ( y> 0 ):
    print("Both numbers are positive")
else: 
    print("not positive")

sum = x + y
if sum < 100 :
    print("Sum is less than 100")
else:
    print("not less")


# question 7 

ch = int ( input ("Enter a single digit:"))

match ch:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2 :
        print("Two")
    case 3:
        print ("Three")
    case 4 :
        print("Four")
    case 5:
        print ("Five")
    case 6 :
        print("Six")
    case 7 :
        print("Seven")
    case 8 : 
        print ("Eight")
    case 9 :
        print ("Nine ")
    case _:
        print( "invalid number ")

#question 10 
passw = input ("Enter your password :")
if 8 <= len(passw) <= 16 :
    if any(ch.isdigit() for ch in passw):
        print("Password valid ")
    else:
        print(" invalid -Must contain atleast one digit")
else:
    print("password invalid") 



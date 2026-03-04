# Question 1 

while True:
    num = int (input("Enter a three digit number :"))
    if len(str(num)) > 3:
        print ("invalid Numbers")
        continue 
    h = ((num //100)% 10)
    t = ((num//10)%10)
    o = (num % 10) 
    if h == t== o:
        print("Not distinct")
    else:
        print("Distinct digits ")

#Question 2 
    if t < h  and t < o :
       print("Middle digit is the largest ")
    elif t< h and t < o:
        print ("Middle digit is the smallest")
    else:
        print("Neither largest or smallest")


# Question 3

num = 8968
th = ((num //1000) % 10)
o = ( num % 10)
if th == o :
    print("First and last digits are equal")
else:
    print("not equal")

# Question 4
num = int (input("Enter your number :"))
digits = len(str(num))
match digits:
    case 1 :
        print("Single digits")
    case 2 :
        print("Double digits")
    case _3:
        print("Multi digits ")


# Question 5

num = 217
if (num % 7) == 0:
    print("Multiple of seven ")
else:
    print("Not a multiple of 7 ")

if (num % 10) == 7 :
    print("ends with 7")
else:
    print("Not ends with 7")

# Question 6 

x,y = map(int, input("Enter x and y coordinates : ").split())

if x > 0 and y > 0:
    print ("Point lies in first quadrant")
elif x < 0 and y > 0:
    print("Point Lies in second quadrant")
elif x < 0 and y < 0:
    print("Point lies in third quadrant")
else:
    print ("Point lies in Fourth quadrant ")


# Question 7 

amount = int (input("Enter your amount :"))
if ( amount % 2000 )== 0:
    print (f"amount can evenly divided. needed {amount // 2000} notes")
else: 
    print(" Can't divided evenly")
if (amount % 500 ) == 0:
    print(f"Can divided evenly. needed {amount // 500} notes ")
else:
    print("can't divided")

if (amount % 100 ) == 0:
    print(f"Can divided evenly. needed {amount // 100} notes ")
else:
    print("can't divided")

# Question 9 

a,b = map(int, input("Enter the two angles of the triangle :").split())

c = 180 - ( a+ b)
print(f"Third angle of the triangle is {c} ")

#Question 10 

num = int (input("Enter your number :"))
root = (num ** 0.5)

if (root * root) == num:
    print("the Number is a perfect square")
else:
    print("Not a perfect square ")
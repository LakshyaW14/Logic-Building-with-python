# Question 1
# x,y = map(int, input("Enter x and y coordinates :").split())
# if  ( x == 0 and y == 0):
#     print("The point lies on origin")
# elif ( x == 0 ):
#     print("The point lies on y-axis")
# elif (y == 0):
#     print("The point lies on x-axis ")
# else:
#     print("neither on x and y axis nor on origin")

#Question 2

# x,y,z = map(int , input ("Enter three numbers : ").split())

# if (( x*x ) + (y*y)) == (z*z):
#     print("Is a pythagorean triplet")
# else:
#     print ("Not a pythagorean triplet ")

#Question 3 
# day, month= map( int, input("Enter day and month :").split())
# days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,7:31, 8:31, 9:30,10:31,11:30,12:31}

# if not ( 1<= month <= 12):
#     print ("Invalid month")
# # print(days_in_month[month])

# if day <= (days_in_month[month]):
#     print("Valid date")
# else:
#     print("Invalid date")

# Question 4
# while True: 
#     hour, min = map(int, input("Enter hour and min :").split())
#     hour_position = hour * 30
#     min_position = min * 6
#     angle = abs(hour_position - min_position)          
#     print(f"The smaller angle between the hour and min hand will be {angle} degree")

#question 5 and 6
# x,y,z = map(int, input("Enter three numbers :").split())

# if (y -x ) == ( z - y):         # common difference
#     print("are in arithmetic progression")
# if (y/x) == (z/y):          #common ratio
#     print("are in geometric progression")



    #Question  7

# num = 257
# h = ((num//100)%10)
# t = (num // 10)%10
# o = ( num % 10)

# if ( h + o) == t:
#     print("true")
# else:
#     print("false")

#Question 8
# num = 1234
# num=abs(num)

# digit_sum = 0
# digit_product = 1

# while num > 0:
#     digit = num % 10
#     digit_sum += digit
#     digit_product *= digit
#     num //=10
# print(digit_product, digit_sum)
# if digit_sum > digit_product:
#     print ("sum is greater than product")
# else:
#     print("Not greater ")


#Question 9 

day,month = map(int,input("Enter first date ( day and month) :").split())
first_date = (day,month)
day_,month_ = map(int,input("Enter second date ( day and month) :").split())
second_date = (day_,month_)

if first_date<second_date:
    print("First date")
elif first_date>second_date:
    print("Second date")
else:
    print ("both dates are same")

# if (first_date[1] <= second_date[1]) and (first_date[0] <= second_date[0]):
#     print ("First date comes first in the calender ")
# else:
#     print("second date comes first in the calender ")
#Question 10

# year = int(input("enter the year :"))
# print(f"{(year //100) + 1} th century ") 


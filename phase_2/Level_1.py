#Question 1
def print_num():
    for i in range(1,11): print(i, end=' ')
    num =1
    while num <= 10: 
        print(num , end= ' ')
        num +=1

#Question 2
def even_num():
    for i in range(101):
        if i % 2 == 0:
            print(i, end=' ')


#Question 3
def odd_num():
    for i in range(101):
        if i % 2 != 0:
            print(i, end=' ')

#Question 4
def num_down():
    for i in range(10,0,-1): print(i)

#question 5

def table(n):
    for i in range (1,11): print(f"{n}x{i}={n*i}")

#Question 6 
def sum_num(n):
    for i in range (1,n,1):
        n+=i
    print(n)

#Question 7

def  sum_odd(n):
    sum=0
    for i in range (1,n):
        if i % 2 != 0:
            sum+=i
    print(sum)

#Question 8
def  sum_even(n):
    sum=0
    for i in range (1,n):
        if i % 2 == 0:
            sum+=i
    print(sum)
            

def sum_even_pythonic(n):
    print(sum(range(2,n,2)))

#Question 9
def fact(n):
    return 1 if n==0 else n*fact(n-1)


  #Question 10
def product_of_digit(n):
    n = abs(n)
    product = 1
    # while n >0:
    #     digit = n% 10    
    #     product *= digit
    #     n//= 10
    for digit in str(n):
        product *= int(digit)
    return product

import math
def product_pythonic(n):
    return math.prod(int(d) for d in str(abs(n)))

print(product_pythonic(521))
print(product_of_digit(321))


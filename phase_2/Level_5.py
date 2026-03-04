#Question 1
def print_num(n):
    for num in range(1, n + 1):
        digits_sum = 0
        number = num   # copy of num
        
        while number > 0:
            digit = number % 10
            digits_sum += digit
            number //= 10
        
        if digits_sum % 2 == 0:
            print(num, end=" ")


def digit_even_sum_py(n):
    for num in range (1,n+1):
        if sum(map(int, str(num))) % 2 ==0:         # map( function , iterable )
            print(num, end=" ")
    
# digit_even_sum_py(100)




#Quesion 2
def count():
    count = 0
    for i in range(1,201):
        
        if i % 7 == 0 and i % 5 != 0:
            count +=1
        
    return count

#Question 3 

def print_pallindrome(n):
    for i in range(1,n+1):
        reverse_num = int(str(i)[::-1])
        if i == reverse_num:
            print(i)

# print_pallindrome(500)
from Level_2 import pallindrome_py

# print(pallindrome_py(121))


#Question 4 
def print_num_mult(n):
    for i in range(1,n+1):
        if sum(map(int,str(i))) % 3 ==0:
            print(i, end=" ")
# print_num_mult(100)



#Question 5 
def digit_compare(n):
    smallest = 9
    largest = 0
    while n > 0:
        digit = n % 10

        if digit < smallest:
            smallest = digit
        if digit > largest:
            largest = digit
        n //= 10
    print("Smallest digit ", smallest ," and largest digit :", largest)

# digit_compare(234567)

def digit_compare_py (n):
    digits= tuple(map(int,str(n)))
    print(digits,"  ")
    print("Smallest digit :", min(digits))
    print("Largest digit :", max(digits))



#Question 6 

def even_binary_rep(n):
    
    for num in range(1,n+1):
        if format(num,'b').count('1') % 2 == 0:
            print(bin(num)," " ,num)
    
# even_binary_rep(10)


#Question 7 
def pattern (n):
    for i in range (1,n+1)  :print(f"The {i} row " ,i*i ,{"*"*(i*i)})

#Question 8
def factorial(n):
    fact = 0
    while n>0: 
        fact += n
        n -= 1
    return (fact)


#Question 9 

def print_odd_even(n):
    even_digit = 0
    odd_digit = 0
    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 0:
            even_digit += digit
        if digit % 2 != 0:
            odd_digit += digit
    return ( even_digit, odd_digit)    

def print_odd_even_py (n):
    digits = list(map(int, str(n)))
    even = sum( d for d in digits if d % 2 == 0)
    odd = sum ( d for d in digits if d % 2 != 0)
    return even , odd


 #Question 10 

total = 0
for i in range (5):
    num = int(input("Enter a number "))

    if num == 0 :
        continue
    total += num
print("Sum of non zero numbers ", total)
    

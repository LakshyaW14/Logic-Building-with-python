#Question 1 
def count_digit(n):
    n=abs(n)
    count=0
    for digit in str(n):
        count+=1
    return count


#Question 2
def reverse_num(n):
    n = (abs(n))
    reverse_num= 0
    while n>0:
        digits = n%10
        reverse_num = reverse_num*10 + digits
        n//=10
    return reverse_num

def reverse_num_py(n):
    reverse = int(str(n)[::-1])
    return reverse

#question 3 

def pallindrome_py(n):
    reverse = int(str(n)[::-1])

    return True if n == reverse else "Not pallindrome"

#question 4 
def sum_digits_py(n):
    return sum( int(d) for d in str(n) )

#Question 5 
def armstrong_num(n):
    temp = abs(n)
    digits=len(str(n))
    total =0
    while temp >0:
        digit = temp %10
        total += digit**digits
        temp//=10
    return total == n

def armstrong_py(n):
    s = str(abs(n))
    power = len(s)
    return sum( int (d) ** power for d in s)==n


#Question 6
def is_perfect(n):
    if n<0:
        return False
    divisor_sum = 0
    for i in range(1,n):
        if n % i == 0:
            divisor_sum +=i
    return divisor_sum == n

#Question 7
def prime_num(n):
    for i in range(1,n):
        if i % 2!=0:
            print (i,end =" ")


#Question 9
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b

#Question 10
def fibonacci_sum(n):
    a,b = 0,1
    fib_sum = 0
    for i in range(n):
        fib_sum +=a
        a,b=b,a+b
    return fib_sum

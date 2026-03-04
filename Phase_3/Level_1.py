#Question 1

def print_num (n):
    if n  == 0:
        return
    print_num(n-1)
    print(n)


#Question 2 

def print_num_down(n):
    if n==0:
        return
    print(n)
    print_num_down(n-1)


#Question 3 

def print_even (n):
    if n  == 0:
        return
    print_even(n-1)
    if n % 2 ==0:
        print(n)

#Question 4 

def print_odd (n):
    if n  == 0:
        return
    print_odd(n-1)
    if n % 2 !=0:
        print(n)

#Question 5 

def sum_num (n):
    if n  == 0:
        return 0
    return n + sum_num(n-1)



#Question 6 

def fact_num (n):
    if n  == 0 or n == 1:
        return 1
    return n * fact_num(n-1)


#Question 7 

def pow_num (x,n):
    if n  == 0:
        return 1
    return  x* (pow_num(x,n-1))

#Question 8 

def fib_num (n):
    if n == 0:
        return 0
    if n ==1 :
        return 1
    return fib_num(n-1) + fib_num(n-2)

#Question 9 

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def print_series(terms):
    for i in range(terms):
        print(fib(i), end=" ")


#Question 10 

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n//10)

print(sum_digits(234))
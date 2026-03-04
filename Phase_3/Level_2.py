#Question 1 

def count_digits (n):
    n = abs (n)
    if n == 0:
        return 0
    return 1 + count_digits(n //10)

#Question 2

def reverse_num ( n):
    n= abs(n)
    if n < 10:
        return n
    last_digit= n %10
    remaining= (n//10)
    return last_digit * 10**(count_digits(remaining)) + reverse_num(remaining)

#Question 3 

def pallindrome(n):
    n = abs(n)
    return True if n == reverse_num(n) else "Not PAllindrome"

def pallidrome_py(n):
    return str(abs(n)) == str(abs(n))[::-1]

#Question 4 
def product_num(n):
    if n == 0:
        return 1
    return n % 10 * product_num(n//10)

#Question 5 
def hcf(x,y):
    if y == 0:
        return x
    return hcf(y,x%y)

# 
#Question 6 

def to_bin(n):
    if n < 2:
        return str(n)
    return to_bin (n//2) + str(n%2)

#Question 7
def print_num_words(n):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    if n == 0:
        return "Zero"
    def helper (num):
        if num == 0:
            return 
        helper(num//10)
        print(words[num%10], end=" ")
    helper(abs(n))
    


#Question 8 
def sum_nth_even (n):

    if n == 0:
        return 0
    return 2*n + sum_nth_even(n-1)
    
#Question 9 
def sum_nth_odd (n):

    if n == 0:
        return 0
    return  (2*n - 1)+sum_nth_odd(n-1)

#Question 10 
def ncr (n,r):
    if r == 0 or r == n:
        return 1
    if r > n:
        return 0 
    return ncr(n-1, r-1) + ncr(n-1,r)

print(ncr(5,2))
#Question 1

def pattern_line (n):
    if n==0:
        return 
    pattern_line(n-1)
    print(5*("*"))

#Question 2 

def pattern_square (n,m):
    
    if m ==0: 
        return
    print((" * ")*n)
    pattern_square(n,m-1)


#Question 3 

def pattern_triangle(n, i=1):
    if i > n:
        return
    spaces = n - i
    stars = 2*i -1
    print("-"*spaces + "*"*stars)
    pattern_triangle(n, i+1)


#Question 4 
def pattern_tri_down(n,i=1):
    if i > n:
        return
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    pattern_tri_down(n,i+1)
    print(spaces + stars)


#Question 5 
def print_row(i,j=1):
    if j>i:
        return
    print(j,end=" ")
    print_row(i,j+1)
def pattern (n ,i=1):
    if i>n :
        return
    print_row(i)
    print()
    pattern(n,i+1)

#Question 6 
def reverse_tri(n,i=1):
    if i> n: return
    stars = "* "*(i)
    
    reverse_tri(n,i+1)
    print(stars)
    

#Question 7 

def mult_table(n,i=1):
    if i >10 : return
    print(n ,"x", i, "=", n*i )
    mult_table(n,i+1)

#Question 8 

def num_(n, i=1):
    if i > n:
        return 
    print(i, end=" ")
    num_(n, i+1)
    print(i,end=" ")

#Question 9 

def sum_recursive(n):
    if n==0: return 0
    result = n + sum_recursive(n-1)
    print(f"sum ({n}) = {n} +sum({n-1}) = {result}")
    return result
    # print(sum_num)

#Question 10

def char_print(i,j=0):
    if j ==i:
        return 
    print(chr(ord('A') + j), end=" ")
    char_print(i,j+1)

def pattern(n,i=1):
    if i > n: return
    char_print(i)
    print()
    pattern(n,i+1)
pattern(6)
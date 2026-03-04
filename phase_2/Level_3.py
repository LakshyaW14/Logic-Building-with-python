#Question 1
def square_num (n):
    for i in range(1, n+1):
        print(i**2)   #print(i**3) for cube


#Question 3
def print_num(a,b):
    for i in range(a,b+1):
        if i%7 ==0:
            print(i)
# print(print_num(2,40))
#Question 4 

def hcf_num(a,b):
    a,b = abs(a), abs(b)
    smallest = min (a,b)
    hcf_value = 1

    for i in range ( 1, smallest+1):
        if a % i == 0 and b % i == 0:
            hcf_value=i
    return hcf_value


def hcf_py(a,b):
    while b != 0:
        a,b = b, a%b
    return a

#Question 5 

def lcm(a,b):
    a,b = abs (a), abs(b)
    greater = max(a,b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += max(a,b)



#Question 6,7
def factor_num (n):
    factor_sum=0
    print("Factors are ")
    for i in range (1,n+1):
        if n % i == 0 :
            factor_sum  += i
            print(i, end=" ")
    return print("the sum of factors are : ",{factor_sum},end="/n")
    
#Question 8
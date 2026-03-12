#Question 1 

def reverse_string (str):
    if len(str) <=1:
        return str
    return  reverse_string(str[1:]) + str[0]
    #  or index based   i=0
    # reverse_string(str, i+1)+ str[0]

#Question 2 

def IsPallindrome(s):
    s=s.lower()
    if len(s) == 0 or len(s) == 1: return True
    if s[0] == s[-1]:
        return IsPallindrome(s[1:-1])
    return False

#Question 3 
def count_vowels(s):
    vowels= ("a","e","i","o","u")
    if len(s)< 1: return 0
    count=0
    if s[0] in vowels:
        count +=1
    #count= i if s[0] in vowela else 0
    return(count) +count_vowels(s[1:])



#Question 4 
def Remove_Space(s):
    if len(s)< 1: return s 
    string = "" if s[0] == " " else s[0]       #if not s: return s
    return string + Remove_Space(s[1:])
    

#Question 5

def ReplaceAToX(s):
    s=s.lower()         #prob: .lower() is called in every recursive funtion 
    if len(s)< 1: return s 
    string = "x" if s [0] == "a" else s[0]
    return string + ReplaceAToX(s[1:])  # Slicing + str Concatenation O(n^2) TC  


def Replace_optimized (s):  #Tc O(n)   List Accumulation 
    s = s.lower()
    result = []
    def helper (i):
        if len(s) == i: 
            return ""
        result.append("x" if s[i] == "a" else s[i])
        helper (i+1)                #Avoid Concatenation 
    helper(0)
    return "".join(result)


#Question 7
def print_char (s,i=0):
    if len(s) == i : return ""
    return s[i] + print_char(s,i+1)
#   return s[0] + print_char (s[1:])

#Question 9;

def To_uppercase (s,i=0):
    if len(s) == i: return ""
    char = s[i].upper()
    return char + To_uppercase(s,i+1)

#Question 10
def count_V_C(s,i=0):
    vowels= ("a","e","i","o","u")
    if  len(s) == i : return 0,0

    v_count,con_count = count_V_C(s,i+1)        #With silicing s[1:] TC is O(n^2)

    if s[i] in vowels:
        return v_count +1 , con_count
    else:
        return v_count, con_count +1
    
    #Tc O(n)


#Question 11
#Divide and Conquer - Binary Search

def Binary_Search (a, x, left=0, right=None):
    
    if right is None:
        right = len(a)-1
    if left > right: 
        return -1
    mid = left + ((right-left)//2)
    if a[mid]== x:
        return mid
    return Binary_Search(a,x,left, mid-1) if x < a[mid] \
        else Binary_Search(a,x, mid+1, right)
    
print(Binary_Search([-1,0,1,4,6,8,9,11], 9))

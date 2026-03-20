# command for installing numpy - pip install numpy

import numpy as np
#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

arr = np.array([ 1,3,4,5,6])
print(type(arr))

# checking version of np 
print(np.__version__)

#Dimensions in array 
#A dimension in arrays is one level of array depth (nested arrays).

# 0-D Array or scalers, each value is a 0D  array
arr0=np.array(34)
print(arr)

# 1-D Array or uni -Dimensional array ( 0-D arr as it's elements)
arr1 = np.array([1,2,3,4,5,6])

# 2-D array ( 1-D as it's elements)
arr2 = np.array([[1,2,3], [5,6,7]])

# 3-D Array ( 2-D array as it's elements)
arr3 = np.array([[[1,2,3,], [2,3,4]], [[1,2,3],[23,34,5]]])
print(arr)

# check number of dimensions 
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
# returns an integer that tell us , how many dimensions 

# Higher number of array 

arr_ =np.array([1,2,3,4], ndmin=5)
print(arr_)
print("number of dimensions :",arr_.ndim)

#in this innermost D has 4elements
#the 4th D has 1 elements, that is the vector
#the 3rd D has 1 elements, that is a mat with vector 
#the 2nd D has 1 element, that is 3D arr
# ths 1st D has 1 ele, that is a 4D arr

# Accessing arr elements 
arr = np.array([ 1,3,4,5,6])
print(arr[0])
print(arr[2] + arr[3]) # it add the two element, not concatenate

# Accessing arr elements  2d 

arr2 = np.array([[1,2,3], [5,6,7]])
print("3rd ele on 1st row", arr2[0,2])

arr3 = np.array([[[1,2,3,], [2,3,4]], [[1,2,3],[23,34,5]]])
print(arr3[0,1,1]) 
# 2nd element of second arr of first arr

# Negative Indexing 
arr2 = np.array([[1,2,3], [5,6,7]])
print("Last element from 2nd arr", arr2[1,-1])

# Array Slicing 
arr1 = np.array([1,2,3,4,5,6])
print(arr1[1:5:2])
print(arr1[-3:-1])

 # Slicing 2D arr
arr2 = np.array([[1,2,3], [5,6,7]])
print(arr2[0, 0:2])
print(arr2[0:2,2])
print(arr2[0:2,0:1])


# Checking the DataType 
arr_str =np.array(["apple", "kiwi"])
print(arr_str.dtype)
print(arr.dtype)

# Creating arrays with a defined Data Type 

arr = np.array([1,2,3], dtype= 'S')
arr_ = np.array([1,2,3], dtype= 'i4') # i,u,f,s,and u define with size 
print(arr)
print(arr_.dtype)
print(arr.dtype)

# Convwerting DataType existing on Existing arr 

#arr_ = np.array([1,2,a], dtype= 'i4') # This 'a' will give value error
#bestpractice 
# Best way is to make a copy of the arr , with astype()
arr = np.array([1.1, 2.1, 3.1])
new_arr = arr.astype('i') # 'int' parameter 
print(new_arr)
print(new_arr.dtype)

# Array Copy and Array View 
# copy is the new array 
#view is just a view of the original arr 
print()

arr = np.array([1.1, 2.1, 3.1])
x=arr.copy()
arr[0] =42
print(arr)
print(x)

print()
y =arr.view()
arr[1] = 34
print(arr)
print(y)
#changes in view , the original arr is affected 
y[0]= 56
print(arr)
print(y)

#check if the array owns its data
# if it owns, returns NONE otherwise the original object

print(x.base) # copy returns none 
print(y.base) # view returns original object 

# Get the shape of an array

arr2 = np.array([[1,2,3], [5,6,7]])
print(arr2.shape) # Returns a tuple (2,3) means that the arr has 2 d, 
print()
# Reshape array 
arr= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
newarr_3d= arr.reshape (2,3,2)
print(newarr)
print(newarr_3d)

# return copy or view 
print(newarr.base)

# Unknown Dimensions --not need to specify one dimension 
new_arr = arr.reshape(2,2,-1)
print(new_arr)
print()

#flattening the arr 
flat_arr = arr.reshape(-1)
print(flat_arr)
print()

# iterating Arrays 
for x in newarr:
    print(x, end=" ")

for x in arr3:
    for y in x:
        for z in y:
            print(z)

# iterating using nditer()
#  In basic for loops, iterating through each scalar of an array we \
# need to use n for loops which can be difficult to write for arrays with very high dimensionality.
# see above example three for loops 

for x in np.nditer(arr3):
    print(x)

#NumPy does not change the data type of the element in-place (where the element is in array)\
#  so it needs some other space to perform this action, that extra space is called buffer, \
# and in order to enable it in nditer() we pass flags=['buffered'].

#Iterating Array With Different Data Types
for x in np.nditer(arr3,flags=['buffered'], op_dtypes=['S']):
    print(x)

#Iterating With Different Step Size

for x in np.nditer(arr2[:, ::2]):
    print(x)

#Enumerated Iteration Using ndenumerate()
# Enumeration means mentioning sequence number of somethings one by one.
# Sometimes we require corresponding index of the element while iterating,\
#  the ndenumerate() method can be used for those usecases.

for idx , x in np.ndenumerate(arr2):
    print(idx,x)

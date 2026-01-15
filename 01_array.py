"""
from array import *

val = array('i',[])         # This is how we initialize an empty array.
val = array('i',[1,2,3,4,5,6,7,8])         # We can store the data in integer format.
val = array('d',[1,2,3,4,5,6,7,8])        # We can store the data in floating number format.
val = array('u',['a','b','c','d','e'])        # We can store data in character format.

for x in val:
    print(x, end=' ')

print('\n')

print(val.typecode)       # This is used to know the typecode of the array.

val.reverse()

for i in range(0,len(val)):
    print(val[i], end=' ')

val.insert(2,10)        # The insert function always takes 2 arguments , first argument is for index and then the value which we want to insert into the array

val.append(100)         # Add's the element at the end of the array.

val.pop(3)      # It will remove the element of array from the given index.
val.pop()       # It will remove the element from the end of the array.
val.remove(6)        # We give the value which we want to remove from the array.
i = val.index(6)        # Finds the index of the given element in the array.
print(i)


print('\n')

copyArray = array(val.typecode, (x*2 for x in val))        
for x in copyArray:                                              # Used to make a copy of an already existing array with change in it's values.
    print(x, end=' ')


abc = val[2:5]          # Slicing of an array.

abc = val[::-1]     # Reverse slicing.
for x in abc:
    print(x, end=' ')


n = int(input("How many element's you want to add into array : "))
for i in range(n):
    val.append(int(input("Enter the next number : ")))

for x in val:
    print(x, end=' ')

"""

from numpy import *

val = array([1,2,3.4,'a'])      # By using numpy we can store hetrogeneous datatype items and we also don't need to mention the tycodeof the array.
val = array([1,2,3,4], float)
val = linspace(10,20,5)         # Create's an array starting from 10 and ending with 20 and dividing their difference in 5 equal parts.
val = arange(10,20,2)           # Create's an array starting from 10 and maintains a gap of 2 number's till 19 because here 20 is excluded.
val = logspace(10,20,3)
val = zeros(6)          # Create's an array with six (0) in it.(float)
val = ones(6)           # Create's an array with six (1) in it.(float)
val = full(10,4)          # Create's an array with ten (4) in it. ()
for x in val:
    print(x, end=' ')


# How to form matrix in python using numpy.

zero = array(10)
print(zero)

first = array([1,2,3,4,5])
print(first)

second = array([[1,2],[3,4],[5,6]])
print(second)

third = array([[[1,2],[3,4],[5,6]], [[7,8],[9,8],[7,6]]])
print(third)
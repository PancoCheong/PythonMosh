import numpy as np
# 1-D array
array = np.array([1, 2, 3])
print(array)
print(type(array))
# 2-D array - aka. matrix
array_2d = np.array([[1, 2, 3], [4, 5, 6]])     # 2 rows and 3 columns
print(array_2d)
print(array_2d.shape)                           # output:(2, 3)

# array with all zero value (floating number by default)
array = np.zeros((3, 4))                # shape = 3 rows, 4 columns
print(array)
#
array = np.zeros((3, 4), dtype=int)     # change data type
print(array)
#
# array with all value of 1
array = np.ones((3, 4))                 # shape = 3 rows, 4 columns
print(array)

#
# array with all value of specified number 99
array = np.full((3, 4), 99, dtype=int)   # shape = 3 rows, 4 columns
print(array)
#
# import random
#
# array with random value between 0 and 1
array = np.random.random((3, 4))
print(array)
#
# access the matrix
print(array[0, 0])
#
# conditional check on each item
print(array > 0.4)      # output: bool
#
# filter the output (only > 0.4)
print(array[array > 0.4])
#
# sum of all items
print(np.sum(array))
# math functions
print(np.floor(array))
print(np.ceil(array))
print(np.round(array))
#
first = np.array([[1, 2, 3], [4, 5, 6]])
second = np.array([[11, 12, 13], [14, 15, 16]])
print(first + second)   # add position by position (ie. 1+11, 2+12)
print(first * 3)        # multiple each item
#
# eg. convert inch to cm
numbers_inch = np.array([1, 2, 3])
numbers_cm = numbers_inch * 2.54
print(numbers_cm)
#
# use standard Python list comprehension
numbers_inch = [1, 2, 3]
numbers_cm = [number * 2.54 for number in numbers_inch]
print(numbers_cm)
#
#
#

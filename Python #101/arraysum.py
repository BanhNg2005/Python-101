import math
import numpy as np
import sys

# Function to calculate the sum of an array

def arraysum(arr):
    # Initialize the sum
    sum = 0
    # Loop through the array
    for i in range(len(arr)):
        sum += arr[i]
    return sum

# array to calculate the sum of 

arr = np.array([1, 2, 3, 4, 5])
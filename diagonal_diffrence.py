"""
visit https://www.hackerrank.com/challenges/diagonal-difference/problem to view problem statement
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    left_diagonal = 0
    right_diagonal = 0
    for element in range(len(arr)):
        left_diagonal += arr[element][element]
        right_diagonal += arr[element][len(arr) - element - 1]
    
    answer = left_diagonal - right_diagonal

    return abs(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

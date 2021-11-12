"""
visit https://www.hackerrank.com/challenges/plus-minus/problem for view problem details
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    arr_len = len(arr)
    
    for n in arr:
        if(n>0):
            positives +=1
        if(n<0):
            negatives +=1
        if(n==0):
            zeros +=1 
    
    print("{0:.6f}".format(positives/arr_len))
    print("{0:.6f}".format(negatives/arr_len))
    print("{0:.6f}".format(zeros/arr_len)) 
     
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

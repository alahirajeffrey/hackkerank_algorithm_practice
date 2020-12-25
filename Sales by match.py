# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:53:12 2020

@author: Jeffrey Alahira

Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with 
matching colors there are.

For example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2] 
There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. 
The number of pairs is 2.
"""


#!/bin/python3

import os
from collections import Counter 

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    
    #variable to hold number of sock pairs
    number_of_socks = 0
    socks_count = Counter(ar)
    
    for sock in socks_count:
        number_of_socks += socks_count[sock]//2
    
    return number_of_socks
            
    
if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'sales_by_match.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

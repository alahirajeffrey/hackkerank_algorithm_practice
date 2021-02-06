# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:00:29 2021

@author: Jeffrey Alahira
"""

""""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. 
Each summer, its height increases by 1 meter. A Utopian Tree sapling with a height of 1 meter is 
planted at the onset of spring. How tall will the tree be after  growth cycles?

For example, if the number of growth cycles is n = 5, the calculations are as follows:
    
Period  Height
0          1
1          2
2          3
3          6
4          7
5          14
"""

#!/bin/python3

import os

# Complete the utopianTree function below.
def utopianTree(n):
    
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return (utopianTree(n - 2) * 2) + 1
    else:
        return (utopianTree(n - 2) + 1) * 2

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'file.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

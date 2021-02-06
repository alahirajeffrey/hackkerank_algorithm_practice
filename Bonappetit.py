# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:23:49 2021

@author: Jeffrey Alahira
"""

"""

visit https://www.hackerrank.com/challenges/bon-appetit/problem for problem statement 

"""


#!/bin/python3


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    total = sum(bill) - bill[k]

    if total/2 == b:
        print('Bon Appetit')

    else:
        print(int(b - (total/2)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

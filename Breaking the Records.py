# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:36:11 2020

@author: Jeffrey Alahira
"""

"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array scores = [12,24,10,24]
Scores are in the same order as the games played. She would tabulate her results as follows

                              Count
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1
 
Given the scores for a season, find and print the number of times Maria breaks her records for most 
and least points scored during the season.

SAMPLE INPUT:

9 #number of records to be inputed
10 5 20 20 4 5 2 25 1 #scores of Maria
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    
    n_broken_highest = 0 #hold number of times maria beat high score
    n_broken_lowest = 0 #hold number of times maria went below lowest score
    max_score = scores[0] #set max_score to the first record of the season
    min_score = scores[0] #set min_score to the firsst record of the season
    answer = [] #list to hold number of times maria beat hugh score and number of times she  beat low score

    for score in range(len(scores) -1 ):
        
        if max_score < scores[score + 1]:
            n_broken_highest += 1
            max_score = scores[score + 1]

        elif min_score > scores[score + 1]:
            n_broken_lowest += 1
            min_score = scores[score + 1]
    
    answer.append(n_broken_highest)
    answer.append(n_broken_lowest)
    
    return answer 

if __name__ == '__main__':
    
    os.environ['OUTPUT_PATH'] = 'file.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

   
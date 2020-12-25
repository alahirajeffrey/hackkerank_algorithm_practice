#!/bin/python3

"""
A video player plays a game in which the character competes in a hurdle race. 
Hurdles are of varying heights, and the characters have a maximum height they can jump. 
There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose. 
How many doses of the potion must the character take to be able to jump all of the hurdles. 
If the character can already clear all of the hurdles, return 0.

FUnction discription 

Complete the hurdleRace function in the editor below. HurdleRace has the following parameter(s):

int k: the height the character can jump naturally

int height[n]: the heights of each hurdle

"""
import os

# Complete the hurdleRace function below.
def hurdleRace(k, height):
    
    #get maximum number in the list
    max_number = max(height)
    
    if max_number > k:
        return max_number - k
    
    elif k >= max_number:
        return 0

if __name__ == '__main__':
    
    os.environ['OUTPUT_PATH'] = 'answer.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
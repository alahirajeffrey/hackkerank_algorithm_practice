# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:18:29 2021

@author: Jeffrey Alahira
"""

"""

visit https://www.hackerrank.com/challenges/grading/problem for problem statement
    
"""

#!/bin/python3


import os

def gradingStudents(grades):
    
    for grade in grades:
        
        if (grade < 38):
            yield grade
        
        elif (5 - grade%5) < 3:
            grade = grade  - grade%5  + 5
            yield grade

        else:
            yield grade

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'file.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

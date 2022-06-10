#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades): 
    for x in range(len(grades)): 
        if int(grades[x]) >= 38: 
            for i in range(int(grades[x]),int(grades[x])+10): 
                if i%5 == 0 and i - int(grades[x]) < 3: grades[x] = str(i)
    return(grades)

if __name__ == '__main__':
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

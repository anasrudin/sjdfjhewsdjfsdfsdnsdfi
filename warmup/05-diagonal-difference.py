#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    arrsize = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0 
    # print(math.sqrt(arrsize+1))
    # print(arr[arrsize-1][arrsize-1])
    x = 0
    for i in range(arrsize):
        primary_diagonal= primary_diagonal + arr[i][i]
        secondary_diagonal=secondary_diagonal+ arr[i][arrsize-1]
        arrsize = arrsize - 1
        print(primary_diagonal, secondary_diagonal)
    x = abs(primary_diagonal-secondary_diagonal)
    return (x)
    # print(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    result_dump = [0,0]
    # b_result = 0
    for i in range (len(a)):
        if a[i]==b[i]:
            continue
        elif a[i]>b[i]:
            result_dump[0] = result_dump[0] +1
            print
        elif a[i]<b[i]:
            result_dump[1]= result_dump[1] +1
        else:
            continue
    return(result_dump)
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print ("compareTriplets")
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

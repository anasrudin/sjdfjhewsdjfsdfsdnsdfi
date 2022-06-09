#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max=-sys.maxsize-1
    min=sys.maxsize
    # print (min, max)
    sum=0
    for x in arr:
        sum+=x
        if x>max:
            max=x
        if x<min:
            min=x
    print (sum-max,sum-min)
            
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

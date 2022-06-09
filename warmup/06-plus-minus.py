#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i < 0:
            negative = negative+1
        elif i> 0:
            positive = positive+1
        else:
            zero = zero + 1
    positive_proportion = positive/(len(arr))
    negative_proportion = negative/(len(arr))
    zero_proportion = zero/(len(arr))
    # r(positive_proportion, negative_proportion, zero_proportion)
    print(positive_proportion)
    print(negative_proportion)
    print(zero_proportion)
    return(positive_proportion, negative_proportion, zero_proportion)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

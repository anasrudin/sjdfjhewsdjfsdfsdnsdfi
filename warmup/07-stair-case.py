#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    last_item_pointer = n-1 
    for i in range(n):
        j = i+1
        print((" "*last_item_pointer)+(("#")*j))
        last_item_pointer = last_item_pointer - 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

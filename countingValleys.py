#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c=0
    v=0
    s=s.lower()
    for i in s:
        if i=='u':
            c=c+1
        elif i=='d':
            if c==0:
                v=v+1
                c=c-1
            else:
                c=c-1
    return v           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

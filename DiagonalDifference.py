#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    su=0
    s=0
    length=len(arr)
    for i in range(length):
        for j in range(length):
            if i==j:
                su+=arr[i][j]
    for i in range(length):
        for j in range(length):
            if i+j==length-1:
                s+=arr[i][j]
    return abs(su-s)
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

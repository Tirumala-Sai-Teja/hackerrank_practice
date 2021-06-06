#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
'''def isGp(a,r):
    a1=a[0]
    l=[a1,a1*pow(r,1),a1*pow(r,2)]
    if l==a:
        return True
    else:
        return False
def countTriplets(arr, r):
    for i in arr:
        l=[]
        for j in range(i+1,len(arr)):
            if len(l)<3:
                l.extends([i,j,])'''
from collections import Counter
def countTriplets(arr, r):
    left_map = Counter()
    right_map = Counter(arr)
    count = 0
    for j in arr:
        right_map[j] -= 1
        i = left_map[j/r]
        k = right_map[j*r]
        count += i * k
        left_map[j] += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

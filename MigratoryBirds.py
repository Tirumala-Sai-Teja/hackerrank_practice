#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in arr:
        if i==1:
            a+=1
        elif i==2:
            b+=1
        elif i==3:
            c+=1
        elif i==4:
            d+=1
        elif i==5:
            e+=1
    if a>=b and a>=c and a>=d and a>=e:
        return 1
    elif b>=c and b>=d and b>=e:
        return 2
    elif c>=d and c>=e:
        return 3
    elif d>=e:
        return 4
    else:
        return 5

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

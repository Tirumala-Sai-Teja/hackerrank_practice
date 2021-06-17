#!/bin/python3

import math
import os
import random
import re
import sys
from functools import *
from math import gcd
def lcm(i,j):
    return i*j//gcd(i,j)
def getTotalX(a, b):
    l=reduce(lcm,a,1)
    lcm2=l
    g=reduce(gcd,b)
    c=0
    while(l<=g):
        if g%l==0:
            c+=1
        l+=lcm2
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()


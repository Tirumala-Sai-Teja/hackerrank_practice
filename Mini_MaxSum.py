#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mn=min(arr)
    mx=max(arr)
    arr.remove(mn)
    arr.remove(mx)
    l=[]
    l.append(sum(arr)+mn)
    l.append(sum(arr)+mx)
    s=''
    for i in l:
        s=s+str(i)+' '
    print(s)    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

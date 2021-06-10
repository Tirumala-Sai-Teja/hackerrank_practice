#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    p=0
    iq=0
    count=0
    nq=0
    for a in arr:
        i=a
        p+=1
        while i!=0:
            iq +=1
            nq +=1
            if(iq==p):
                count+=1
            if nq==k:
                if iq!=a:
                    p+=1
                nq=0
            i-=1
    
        iq=0
        nq=0

    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

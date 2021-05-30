#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    s1=s[::-1]
    a=[]
    b=[]
    c=0
    for i in range(len(s)):
        a.append(ord(s[i]))
        b.append(ord(s1[i]))
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1])!=abs(b[i]-b[i+1]):
            return 'Not Funny'
    else:
        return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

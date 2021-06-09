#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s1=s.lower()
    c=0
    a="abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i not in s1:
            c=1
    if c==0:
        return 'pangram'
    else:
        return 'not pangram'
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

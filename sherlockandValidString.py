#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
from collections import Counter
def isValid(s):
    d=Counter(s)
    p=list(d.values())
    k=p[0]
    c=0
    for i in range(1,len(p)):
        if k==p[i]:
            continue
        elif k>1 and c==0 and p[i]==1:
            c+=1
            
        else:
            c+=abs(k-p[i])
    if c<=1:
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

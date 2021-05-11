#!/bin/python3

import math
import os
import random
import re
import sys
def breakingRecords(scores):
    mn,mx=scores[0],scores[0]
    c1,c2=0,0
    for i in range(1,len(scores)):
        if scores[i]<mn:
            mn=scores[i]
            c1+=1
        if scores[i]>mx:
            c2+=1
            mx=scores[i]
    return [c2,c1]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

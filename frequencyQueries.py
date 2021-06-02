#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the freqQuery function below.
def freqQuery(queries):
    l=[]
    for i in queries:
        if i[0]==1:
            l.append(i[1])
        elif i[0]==2:
            if i[1] in l:
                l.remove(i[1])
        else:
            c=Counter(l)
            for j in c.values():
                if i[1]==j:
                    print(1)
                    break
            else:
                print(0)
            '''l2=list(c.values())
            if i[1] in l2:
                print(1)
            else:
                print(0)'''
   
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    freqQuery(queries)

    '''fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()'''

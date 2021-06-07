#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c=[]
    r=0
    s=set(ar)
    for i in s:
       c.append(ar.count(i))
    
   
  
    for i in range(len(c)):
        if c[i]>=2:
            
            r=r+c[i]//2
            
    
    return(r)    
            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

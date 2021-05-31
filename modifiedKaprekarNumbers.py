#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    c=0
    for i in range(p,q+1):
        s=str(i*i)
        if len(s)==1:
            if s==str(i):
                print(s,end=' ')
                c+=1
        else:
            x=int(s[:len(s)//2])
            y=int(s[len(s)//2:])
            if x+y==i:
                print(i,end=' ')
                c+=1
    if c==0:
        print('INVALID RANGE')
        
            
            
              
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

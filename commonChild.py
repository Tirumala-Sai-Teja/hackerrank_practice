#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
#def commonChild(s1, s2):
''' l=[]
    n=0
    p=0
    while n<len(s1):
        c=0
        for j in range(n,len(s1)):
            
            for k in range(p,len(s2)):
                if s1[j]==s2[k]:
                    if c==1:
                        n+=1
                    c+=1
                    p=k+1
                
                    break
        n+=1
        p=0    
        l.append(c)
    print(set(l))
    return max(l)'''
def commonChild(s1, s2):
    m, n = len(s1), len(s2)
    prev, cur = [0]*(n+1), [0]*(n+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        cur, prev = prev, cur
    return prev[n]
                    
                    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

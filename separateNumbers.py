#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
        for i in range(len(s)//2):
            rs=''
            n=int(s[:i+1])
            t=n
            while(len(rs)<len(s)):
                rs=rs+str(t)
                t=t+1
            if rs==s:
             print('YES',n)
             break
        else:
            print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

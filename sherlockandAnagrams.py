#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    dict={}

    count=0

    for i in range(len(s)):

        for j in range(i+1,len(s)+1):

            l1= list(s[i:j].strip())

            l1.sort()

            f=''.join(l1)

            if f in dict: 

                count+=dict[f]

                dict[f]=dict[f]+1

            else:
                 dict[f]=1       

    return count    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    for i in a:
        if i  in b:
            a=a.replace(i,'*',1)
            b=b.replace(i,'*',1)
    print(a)
    print(b)
    return(len(a)-a.count('*')+len(b)-b.count('*'))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

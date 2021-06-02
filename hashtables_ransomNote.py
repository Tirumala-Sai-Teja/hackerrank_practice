#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d=Counter(magazine)
    e=Counter(note)
    f=0
    for i in e:
        if e[i]>d[i]:
            f=1
            break
    if f==1:
        print('No')
    else:
        print('Yes')
            
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

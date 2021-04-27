#!/bin/python3

import math
import os
import random
import re
import sys
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c1=0
    c2=0
    for i in range(m):
        if apples[i]>0:
            if a+apples[i]>=s and a+apples[i]<=t:
                c1+=1
    for i in range(n):
        if oranges[i]<0:
            if b+oranges[i]<=t and b+oranges[i]>=s:
                    c2+=1
    print(c1)
    print(c2)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

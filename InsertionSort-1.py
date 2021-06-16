#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    key=arr[-1]
    f=0
    for i in range(n-2,-1,-1):
        
        if arr[i]<key:
            arr[i+1]=key
            print(*arr)
            f=1
            break
        else:
            arr[i+1]=arr[i]
            print(*arr)
    if f==0:
        arr[0]=key
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

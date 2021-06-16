#!/bin/python3

import math
import os
import random
import re
import sys
def insertionSort2(n, arr):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            ind=i+1
            for j in range(ind):
                if arr[ind]<arr[j]:
                    arr[j],arr[ind]=arr[ind],arr[j]
        print(*arr)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

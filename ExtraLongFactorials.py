#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

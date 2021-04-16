#!/bin/python3

import os
import sys

#
# my logic
#
def pageCount(n, p):
    x=[p//2,n//2-p//2]
    return(min(x))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

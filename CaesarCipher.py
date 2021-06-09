#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    e=''
    for i in s:
        if(i.isalpha()):
            if k>26:
                k=k%26
            x=ord(i)+k
            if(i.islower()):
                if x>ord('z'):
                    x=x-26
            if(i.isupper()):
                if x>ord('Z'):
                    x=x-26
            e=e+chr(x)
        else:
            e=e+i
    return(e)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

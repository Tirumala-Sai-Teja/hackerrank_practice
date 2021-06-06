#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    up= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lo="abcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    sp="!@#$%^&*()-+"
    c=0
    for i in password:
        if i in up:
            c+=1
            break
    for i in password:
        if i in lo:
            c+=1
            break
    for i in password:
        if i in num:
            c+=1
            break
    for i in password:
        if i in sp:
            c+=1
            break
    x=4-c
    k=x+len(password)
    if len(password)>=6 or k>=6:
        return x
    if k<6:
        return 6-len(password)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

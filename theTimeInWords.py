#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    d={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',     10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'quarter',               16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'half',         40:'fourty',50:'fifty'}
    l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30]
    if m==0:
        return(d.get(h)+" o' clock")
    elif m>=1 and m<=30:
        if m not in l:
            a=m
            s=' '
            r=a%10
            s=d.get(r)+s
            a=a-r
            s=d.get(a)+' '+s            
            return(s+'minutes past '+d.get(h))
        else:
            if m==1:
                return(d.get(m)+' minute past '+d.get(h))
            if m==15 or m==30:
                return(d.get(m)+' past '+d.get(h))
            else:
                return(d.get(m)+' minutes past '+d.get(h))
    else:
        mn=60-m
        if mn not in l:
            a=mn
            s=' '
            r=a%10
            s=d.get(r)+s
            a=a-r
            s=d.get(a)+' '+s
            return(s+'minutes to '+d.get(h+1))
        else:
            if mn==15:
                return(d.get(mn)+' to '+d.get(h+1))

            return(d.get(mn)+' minutes to '+d.get(h+1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

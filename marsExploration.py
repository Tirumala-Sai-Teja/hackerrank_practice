#!/bin/python3

import math
import os
import random
import re
import sys



def marsExploration(s):
    count=0
    for i,letter in enumerate(s):
        if i%3==1:
            if letter !='O':
                count+=1
        else:
             if letter!='S':
                count+=1
    return count   
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

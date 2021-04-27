#!/bin/python3

import math
import os
import random
import re
import sys
grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item) 
s=[]   
for i in range(len(grades)):
    if grades[i]>=38:
        n=((grades[i]//5)+1)*5
        if n-grades[i]<3:
            s.append(n)
        else:
            s.append(grades[i])
    else:
        s.append(grades[i])
for i in s:
    print(i)        


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    b=False
    if year>=1700 and year<=1917 and year%4==0:
        b=True
    if year==1918:
        return('26.09.1918')#as 1918 is not a leap year normally we ge 13.09.1918 but after julian calendar agfter jan 31st we get feb 14 which means we included only 15 days in feb so we have to add 13 to it ,13.09.1918+13 days=26.09.1918
        
    if year%400==0 or (year %4 ==0 and year %100!=0):
        b=True
    if b:
        return('12.09.'+str(year))
    else:
        return('13.09.'+str(year))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

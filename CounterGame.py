#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'counterGame' function below.
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
for _ in range(int(input())): 
    print("Richard" if (bin(int(input())-1)[2:].count('1'))%2==0 else "Louise")

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here

    res = 1

    for i in range(len(a)):
        suma1 = 0
        suma2 = 0
        for j in range(len(a)):
            if 0 <= (a[i] - a[j]) <= 1:
                suma1 += 1
            if 0 >= (a[i] - a[j]) >= -1:
                suma2 += 1
        res = max(res, suma1)
        res = max(res, suma1)
            
    return res

if __name__ == '__main__':
    fptr = open("output.txt", 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

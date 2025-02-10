#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positives, negatives, neutro = 0, 0, 0
    n = len(arr)
    
    for i in arr:
        if i == 0:
            neutro += 1
        elif i > 0:
            positives += 1
        else:
            negatives += 1
                
    print(f'{positives/n:.6f}')
    print(f'{negatives/n:.6f}')
    print(f'{neutro/n:.6f}')
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

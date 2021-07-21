# https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    counter=0
    for i in range(n):
        numberOfSwaps = 0
        for j in range(n-1):
            if (a[j] > a[j + 1]): 
                a[j], a[j + 1] = a[j+1],a[j]
                numberOfSwaps+=1
                counter+=1
        if (numberOfSwaps == 0):
            break
    print("Array is sorted in",counter,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
            
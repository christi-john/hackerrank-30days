# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print(len(max(bin(n)[2:].split('0'))))
    
    # binary=bin(n)[2:]    #to remove 0b in the beginning
    # array = binary.split('0')
    # maximum=max(array)
    # print(len(maximum))
    
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'largestNum' function below.
#
# The function accepts following parameters:
#  1. INTEGER num1
#  2. INTEGER num2
#  3. INTEGER num3
#

def largestNum(num1, num2, num3):
    # Write your code here
    list_num = []
    list_num.append(num1)
    list_num.append(num2)
    list_num.append(num3)
    list_num.sort()
    return print(list_num[-1])
    

if __name__ == '__main__':
    num1 = int(input().strip())

    num2 = int(input().strip())

    num3 = int(input().strip())

    largestNum(num1, num2, num3)

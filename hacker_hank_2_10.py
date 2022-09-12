#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'last_fact_digit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def last_fact_digit(n):
    # Write your code here
    result = 1
    if n == 0 or n == 1:
        return 1
    if n > 1:
        for i in range (1, n + 1):
            result = result*i
            
        return result%10

n = int(input())

result = last_fact_digit(n)

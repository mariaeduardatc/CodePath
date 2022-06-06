#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateGrade' function below.
#
# The function accepts INTEGER grade as parameter.
#

def calculateGrade(grade):
    # Write your code here
    if grade >= 93:
        return print("A")
    elif 84 <= grade <= 92:
        return print("B")
    elif 74 <= grade <= 83:
        return print("C")
    elif 65 <= grade <= 73:
        return print("D")
    else:
        return print("F")

if __name__ == '__main__':
    grade = int(input().strip())

    calculateGrade(grade)

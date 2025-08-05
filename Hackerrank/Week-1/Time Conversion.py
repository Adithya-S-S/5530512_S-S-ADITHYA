#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hr=int(s[0:2])
    noon=s[-2:]
    if noon=="AM":
        if hr ==12:
            return("00"+s[2:-2])
        if hr <10:
            return("0"+str(hr)+s[2:-2])
        else:
            return(str(hr)+s[2:-2])
    else:
        if hr !=12:
            hr+=12
        return(str(hr)+s[2:-2])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

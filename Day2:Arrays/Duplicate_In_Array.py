from os import *
from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    arr.sort()
    ans = 0;
    for i in range(n):
        if arr[i] == arr[i+1]:
            ans =arr[i]
            break
    return ans

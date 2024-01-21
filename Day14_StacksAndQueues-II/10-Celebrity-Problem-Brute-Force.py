from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):
    for i in range(0,n):
        c = 0
        for j in range(0,n):
            if i==j:
                continue
            if not knows(i,j) and knows(j,i):
                c+=1
            else:
                break
        if c == n-1:
            return i
    return -1

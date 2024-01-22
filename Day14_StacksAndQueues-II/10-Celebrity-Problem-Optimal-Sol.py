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
    stack = []
    count = 0
    for i in range(0,n):
        stack.append(i)
    
    while count < n-1:
        a = stack.pop()
        b = stack.pop()

        if knows(a,b):
            stack.append(b)
        else:
            stack.append(a)
        count+=1
    c = 0

    for i in range(n):
        if i==stack[-1]:
            continue
        if not knows(stack[-1],i) and knows(i,stack[-1]):
            c+=1
        else:
            return -1
        
    if c == n - 1:
        return stack[-1]

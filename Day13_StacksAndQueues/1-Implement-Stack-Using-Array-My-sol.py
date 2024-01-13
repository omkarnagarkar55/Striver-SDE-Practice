from sys import *
from collections import *
from math import *
from typing import List

class Stack:
    def __init__(self, n: int):
        self.arr = [0]*n
        self.n = n-1
        self.i = -1

    def push(self, num: int):
        if self.i <self.n:
            self.i += 1
            self.arr[self.i] = num

    def pop(self) -> int:
        temp = -1
        if self.i >=0:
            temp = self.arr[self.i]
            self.i-=1
        return temp
    

    def top(self) -> int:
        if self.i!=-1:
            return self.arr[self.i]
        else:
            return -1

    def isEmpty(self) -> int:
        if self.i == -1:
            return 1
        else:
            return 0

    def isFull(self) -> int:
        if self.i == self.n:
            return 1
        else:
            return 0


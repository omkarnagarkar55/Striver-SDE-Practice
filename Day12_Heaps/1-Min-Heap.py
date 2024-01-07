from sys import *
from collections import *
from math import *


def heapify(arr,i):
    n = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2
    mi = i

    if left < n and arr[left] < arr[mi]:
        mi = left
    if right < n and arr[right] < arr[mi]:
        mi = right
    
    if mi != i:
        arr[i], arr[mi] = arr[mi], arr[i]
        heapify(arr, mi)

def minHeap(N: int, Q: [[]]) -> []:
    arr = []
    removed_elements = []

    for query in Q:
        if query[0] == 0:  # Insertion
            arr.append(query[1])
            i = len(arr) - 1
            # Heapify up
            while i > 0 and arr[(i - 1) // 2] > arr[i]:
                arr[(i - 1) // 2], arr[i] = arr[i], arr[(i - 1) // 2]
                i = (i - 1) // 2
                
        else:  # Removing min
            if len(arr) > 1:
                removed_elements.append(arr[0])
                arr[0] = arr.pop()
                heapify(arr, 0)
            elif arr:
                removed_elements.append(arr.pop())

    return removed_elements
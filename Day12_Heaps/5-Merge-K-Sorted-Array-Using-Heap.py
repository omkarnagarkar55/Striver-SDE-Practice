from sys import *
from collections import *
from math import *
import heapq

# TC-O(NlogK) SC-O(K) 
def mergeKSortedArrays(kArrays, k:int):
    min_heap = []
    result = []

    # Initialize the heap with the first element of each array
    for i in range(k):
        if kArrays[i]:
            heapq.heappush(min_heap, (kArrays[i][0], i, 0))

    # Extract the minimum element and add the next element from the same array to the heap
    while min_heap:
        val, array_index, element_index = heapq.heappop(min_heap)
        result.append(val)

        if element_index + 1 < len(kArrays[array_index]):
            heapq.heappush(min_heap, (kArrays[array_index][element_index + 1], array_index, element_index + 1))

    return result
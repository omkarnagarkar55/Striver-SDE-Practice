class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        # Swapping if num1 is bigger. As we want smaller list
        if n > m :
            return self.findMedianSortedArrays(nums2,nums1)
        n1 = n + m
        left = (n1 + 1)//2

        low = 0
        high = n
        
        # Binary Search
        while low <= high:
            mid1 = (low + high) >> 1
            mid2 = left - mid1
            
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            
            if mid1 < n:
                r1 = nums1[mid1]
            if mid2 < m:
                r2 = nums2[mid2]
            if mid1 - 1 >=0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <=r1:
                if n1 % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0
            
            if l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
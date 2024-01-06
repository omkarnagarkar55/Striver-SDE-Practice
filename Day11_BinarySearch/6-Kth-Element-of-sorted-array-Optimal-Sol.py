    def kthElement(self,  nums1, nums2, n, m, k):
        # Swapping if num1 is bigger. As we want smaller list
        if n > m :
            return self.kthElement(nums2,nums1,m,n,k)
        n1 = n + m
        
        # k is greater than n ,then we need atleast k-m from the first array
        low = max(0,k-m)
        
        # if K lesser than n, then we need only k element from the first array
        high = min(k,n)
        
        # Binary Search
        while low <= high:
            mid1 = (low + high) >> 1
            mid2 = k - mid1
            
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
                    return max(l1, l2)
            
            if l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
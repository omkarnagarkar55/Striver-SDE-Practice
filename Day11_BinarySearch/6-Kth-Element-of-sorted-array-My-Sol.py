class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        low = min(arr1[0],arr2[0])
        high = max(arr1[n-1],arr2[m-1])
        
        def upperBound(mat,loc,n):
            lo = 0
            hi = n-1
            ans = n
            while(lo <= hi):
                mid = (lo + hi) >> 1
                if mat[mid] > loc:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans        

         # This function is used to count the total number of element before mid number for each row
        def countSmallerElement(mid):
            count = 0
            for i in [arr1,arr2]:
                count+= upperBound(i,mid,len(i))
            return count
        
        while(low<=high):
            mid = (low + high) >> 1
            #finding the count before mid element
            elementCount = countSmallerElement(mid)
            # Binary search
            if elementCount <= k-1:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
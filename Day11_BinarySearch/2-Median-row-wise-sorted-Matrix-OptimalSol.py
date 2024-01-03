def median(matrix: [[int]], m: int, n: int) -> int:
    low = 9999999999
    high = -1

    # This method returns the count of element before loc(given element)
    def upperBound(mat,loc):
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
        for i in matrix:
            count+= upperBound(i,mid)
        return count

    # Storing the lowest and the highest value in low and high variable
    for i in range(m):
        low = min(low,matrix[i][0])
        high = max(high,matrix[i][n-1])
    
    # require count i.e number of elements before the median
    req = (n*m)//2

    # Calculating the median
    while(low<=high):
        mid = (low + high) >> 1
        #finding the count before mid element
        elementCount = countSmallerElement(mid)
        # Binary search
        if elementCount <= req:
            low = mid + 1
        else:
            high = mid - 1
    
    return low

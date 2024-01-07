def aggressiveCows(stalls, k):
    # Write your code here.
    n = len(stalls)
    stalls.sort()

    high = stalls[n-1] - stalls[0]
    low = 1

    while(low <= high):
        mid = (low + high) >> 1
        if isPossible(stalls,mid,k):
            low = mid + 1
        else:
            high = mid - 1
    return high
    
def isPossible(stalls,minDist,k):
    cowCnt = 1
    last = stalls[0]

    for i in range(1,len(stalls)):
        if stalls[i] - last >= minDist:
            cowCnt+=1
            last = stalls[i]
        
        if cowCnt >= k:
            return True
    
    return False
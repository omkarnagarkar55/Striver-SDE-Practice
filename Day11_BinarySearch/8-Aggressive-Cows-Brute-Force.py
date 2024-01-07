def aggressiveCows(stalls, k):
    # Write your code here.
    n = len(stalls)
    stalls.sort()

    limit = max(stalls) - min(stalls)

    for i in range(1,limit + 1):
        if not isPossible(stalls,i,k):
            return i - 1
    return limit
    
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
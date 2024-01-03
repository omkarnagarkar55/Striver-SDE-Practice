def NthRoot(n: int, m: int) -> int:
    # Using Binary Search

    low = 1
    high = m

    while(low <= high):
        mid = (low + high)//2
        val = mid**n
        if val == m:
            return mid
        elif val > m:
            high = mid - 1
        else:
            low = mid + 1

    return -1
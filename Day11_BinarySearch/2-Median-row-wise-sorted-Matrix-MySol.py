def median(matrix: [[int]], m: int, n: int) -> int:
    
    ll = []
    for i in matrix:
        ll+= i
    
    ll.sort()
    n = len(ll)

    return ll[n//2]
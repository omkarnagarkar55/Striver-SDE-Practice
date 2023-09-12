class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = move(0,0,m,n,0)
        return paths

def move(i,j,m,n,uniquePath):
    if i>m-1 or j>n-1:
        return uniquePath
    if i==m-1 and j==n-1:
        return uniquePath + 1
    
    uniquePath = move(i+1,j,m,n,uniquePath) + move(i,j+1,m,n,uniquePath)

    return uniquePath
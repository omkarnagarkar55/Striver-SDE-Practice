class Solution:
    def findPath(self, m, n):
        # code here
        ans = []
        path = []
        visited = [[0]*n for _ in range(n)]
        
        ways = ["U","D","L","R"]
        visited[0][0] = 1
        
        def ratPath(row,col):
            if row == n-1 and col == n-1:
                ans.append("".join(path[:]))
                return
            
            for i in ways:
                if i == "U":
                    if row!=0 and col!=0:
                        if m[row-1][col]==1 and visited[row-1][col]==0:
                            path.append(i)
                            visited[row-1][col]=1
                            ratPath(row-1,col)
                            path.pop()
                            visited[row-1][col]=0
                
                elif i == "D":
                    if row!=n-1:
                        if m[row+1][col]==1 and visited[row+1][col]==0:
                            path.append(i)
                            visited[row+1][col]=1
                            ratPath(row+1,col)
                            path.pop()
                            visited[row+1][col]=0
                
                elif i == "R":
                    if col!=n-1:
                        if m[row][col+1]==1 and visited[row][col+1]==0:
                            path.append(i)
                            visited[row][col+1]=1
                            ratPath(row,col+1)
                            path.pop()
                            visited[row][col+1]=0
                else:
                    if col!=0 and row!=0:
                        if m[row][col-1]==1 and visited[row][col-1]==0:
                            path.append(i)
                            visited[row][col-1]=1
                            ratPath(row,col-1)
                            path.pop()
                            visited[row][col-1]=0
        if m[0][0]!=0:
            ratPath(0,0)
            
        return ans
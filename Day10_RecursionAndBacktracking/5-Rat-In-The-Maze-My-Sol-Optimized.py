    def findPath(self, m, n):
        if m[0][0] == 0 or m[n-1][n-1] == 0:  # Check if start or end is blocked
            return []
    
        ans = []
        path = []
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
    
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    
        def ratPath(row, col):
            if row == n - 1 and col == n - 1:
                ans.append("".join(path))
                return
    
            for dir, (dr, dc) in directions.items():
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < n and 0 <= newCol < n and not visited[newRow][newCol] and m[newRow][newCol] == 1:
                    path.append(dir)
                    visited[newRow][newCol] = True
                    ratPath(newRow, newCol)
                    path.pop()
                    visited[newRow][newCol] = False
    
        ratPath(0, 0)
        return ans
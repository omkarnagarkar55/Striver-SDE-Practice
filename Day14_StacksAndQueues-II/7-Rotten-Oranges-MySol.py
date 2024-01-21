class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m = len(grid)
        n = len(grid[0])
        count=fo=fo1 = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fo+=1

        if len(queue) == 0 and fo == 0:
            return 0
        else:
            while queue:
                s = []
                while queue:
                    posi,posj = queue.pop()

                    # left
                    if posj+1 < n and grid[posi][posj + 1] == 1:
                        grid[posi][posj + 1] = 2
                        s.append([posi,posj+1])
                        fo1+=1
                    
                    # down
                    if posi + 1 < m and grid[posi + 1][posj] == 1:
                        grid[posi + 1][posj] = 2
                        s.append([posi + 1,posj])
                        fo1+=1
                    
                    # right
                    if posj - 1 >= 0 and grid[posi][posj - 1] == 1:
                        grid[posi][posj - 1] = 2
                        s.append([posi,posj - 1])
                        fo1+=1

                    # up
                    if posi - 1 >= 0 and grid[posi - 1][posj] == 1:
                        grid[posi - 1][posj] = 2
                        s.append([posi - 1,posj])
                        fo1+=1
                
                count+=1
                queue = s[:]

        if fo1 == fo:
            return count - 1
        else:
            return -1
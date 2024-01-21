from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0

        # Initialize the queue and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        if not queue and fresh_oranges == 0:
            return 0

        minutes = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_oranges -= 1
                        if fresh_oranges == 0:
                            return minutes + 1

        return -1 if fresh_oranges > 0 else minutes

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -1
        n = len(heights)
        l = [-1] * n
        r = [-1] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                l[i] = 0
            else:
                l[i] = stack[-1] + 1
            
            stack.append(i)
        
        while stack:
            stack.pop()

        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                r[i] = n-1
            else:
                r[i] = stack[-1] - 1
            stack.append(i)
        
        for i in range(n):
            maxArea = max(maxArea,heights[i] * (r[i]-l[i] + 1))
        
        return maxArea

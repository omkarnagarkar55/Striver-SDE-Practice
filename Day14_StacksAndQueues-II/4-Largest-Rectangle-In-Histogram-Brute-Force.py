class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -1
        n = len(heights)
        for i in range(n):
            left = right = i
            while left >= 0:
                if heights[left] >= heights[i]:
                    left-=1
                else:
                    break
            while right < n:
                if heights[right] >= heights[i]:
                    right+=1
                else:
                    break
            area = heights[i] * (right - left - 1)
            maxArea = max(area,maxArea)
        
        return maxArea
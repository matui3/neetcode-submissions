class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        area = 0
        while l <= r:
            width = r - l
            currArea = min(heights[l], heights[r]) * width
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            area = max(currArea, area)
        return area
            
            
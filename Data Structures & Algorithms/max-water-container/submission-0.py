class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to iterate through array
        # use two pointers with sliding window of variable size
        l, r = 0, len(heights) - 1
        # need a variable to keep track of area
        maxArea = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxArea
            
            
            


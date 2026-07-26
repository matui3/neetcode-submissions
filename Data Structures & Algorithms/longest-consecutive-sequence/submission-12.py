class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put all of these in a set
        numbers = set(nums)
        longest = 0
        for num in nums:
            length = 1
            while (num + length) in numbers:
                length += 1
            longest = max(longest, length)
        
        return longest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # create a variable to keep track of longest
        longest = 0
        # keeps track of what elements are in my sequence
        numSet = set(nums)

        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

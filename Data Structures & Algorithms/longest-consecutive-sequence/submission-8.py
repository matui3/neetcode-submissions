class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # create a variable to keep track of longest
        longest = 0
        # keeps track of what elements are in my sequence
        element_tracker = set(nums)

        for num in nums:
            current_longest = 1
            while (num + 1) in element_tracker:
                current_longest += 1
                num += 1
            longest = max(current_longest, longest)
        
        return longest

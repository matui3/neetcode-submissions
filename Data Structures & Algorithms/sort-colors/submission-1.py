class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # frequency map of numbers 0, 1, 2.
        # each index represents the occurence in nums
        count = [0] * 3

        # place each item into frequency map for number of occurrences. 
        # Can use a list of range 3 instead of a map
        for num in nums:
            count[num] += 1
        
        # now use for i in range 3 as you want for each number to change numbes
        index = 0
        for i in range(3):
            # basically while this isn't 0, you increment an index
            while count[i] != 0:
                count[i] -= 1
                nums[index] = i
                index += 1

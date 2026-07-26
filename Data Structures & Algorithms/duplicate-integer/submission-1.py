class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # need a frequency map
        hashmap = {}
        # need to iterate through the array
        for i in range(len(nums)):
            if nums[i] in hashmap: # if its in the hashmap, check and return false
                return True
            else:
                hashmap[nums[i]] = 1 # if not, put it in map
        # false
        return False
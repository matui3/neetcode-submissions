class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        product = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n-1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)- 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(n):
            product[i] = prefix[i] * suffix[i]

        return product
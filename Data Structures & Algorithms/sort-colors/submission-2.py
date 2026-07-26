class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = one_count = two_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1
        i = 0
        while zero_count != 0:
            nums[i] = 0
            i += 1
            zero_count -= 1
        
        while one_count != 0:
            nums[i] = 1
            i += 1
            one_count -= 1
        
        while two_count != 0:
            nums[i] = 2
            i += 1
            two_count -= 1

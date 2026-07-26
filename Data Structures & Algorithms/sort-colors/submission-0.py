class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        # get the count of each number in nums
        for num in nums:
            count[num] += 1
            # basically count[0] will take the count of 0 so that every time, 0 is in nums, it increments
            # same with count[2]. whenever 2 is shown, it increases that count
        
        # now start modifying the array
        index = 0
        for i in range(3): # for each number in 0,1,2
            while count[i]: # while the value is not 0
                count[i] -= 1 # decrease the value of that number
                nums[index] = i # make that index that value
                index += 1
    

        
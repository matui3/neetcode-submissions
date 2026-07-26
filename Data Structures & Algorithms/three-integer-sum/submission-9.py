class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletsList = []
        nums.sort()

        for index, value in enumerate(nums):
            if value > 0:
                break
            
            if index > 0 and value == nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1

            while l < r:
                tripletSum = value + nums[l] + nums[r]

                if tripletSum < 0:
                    l += 1
                elif tripletSum > 0:
                    r -= 1
                else:
                    tripletsList.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
            
        return tripletsList





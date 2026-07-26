class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # must sort the array
        nums.sort()

        # a list to store triplets
        triplets = []
        # use two pointers to check for things
        

        # must iterate over array
        # basically if sorted once all things are in order if the values are all positive, cannot equal 0
        for i, a in enumerate(nums):
            if a > 0:
                break

            # if you're past the first index and your current valueis the same as the last one, skip
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r: # must be distinct
                threeSum = nums[l] + nums[r] + a

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    triplets.append([nums[l], nums[r], a])
                    l += 1
                    r -= 1
                    # if you have two of the same value and l < r after appending, move l forward
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return triplets
                



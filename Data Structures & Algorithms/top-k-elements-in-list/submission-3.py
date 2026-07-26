class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize a frequency map
        count = {}
        
        # need a bucket list where the length determines number of buckets
        # this is because for example if you have a number that occurs 1 time, then itll be in the 1 bucket.
        # But if it occurs 7 times, it should go to the 7 bucket 
        bucketList = [[] for i in range(len(nums)+1)] 

        # go through each nubmer, that is going to create a key value pair where it counts the number occurrences in the list
        for i in nums:
            count[i] = count.get(i, 0) + 1

         # iterate through
        for num, cnt in count.items():
            # the count of that item should append that number
            bucketList[cnt].append(num)
        
        result = []
        # go through every item in the bucket list and i want the item inside that bucket 
        for i in range(len(bucketList) - 1, 0, -1):
            for number in bucketList[i]:
                result.append(number)
                if len(result) == k:
                    return result
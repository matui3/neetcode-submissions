class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqBucketList = [[] for i in range(len(nums) + 1)] # need a bucket for when the frequency is the len of list

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            freqBucketList[cnt].append(num)
        
        res = []
        for i in range(len(freqBucketList) -1, 0, -1):
            for num in freqBucketList[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
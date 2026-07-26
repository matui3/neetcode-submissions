class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need to count the frequencies
        count = {}
        # create buckets to organize numbers based on frequency
        # use len(nums) + 1 as you want 0 to len(nums). 0 isn't used
        freq = [[] for i in range(len(nums) + 1)]

        # get the frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # now place in the buckets
        for value, occurrences in count.items():
            freq[occurrences].append(value)

        # now use this to get a resulting array
        # start at the end of the frequency array
        # use len(freq) - 1 as this is the len(num) index.
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
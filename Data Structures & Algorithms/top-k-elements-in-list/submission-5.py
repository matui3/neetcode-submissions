class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i need the k most frequent

        # the way we do this is to count it in buckets

        freq = {}
        # maps frequency of a number to the value
        buckets = [[] for i in range(len(nums) + 1)]

        # lets get frequencies
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        # now we add this to the buckets
        # both the key and value pair. now the value is the "key" and the "keys" are the values
        for number, occurrence in freq.items():
            buckets[occurrence].append(number)
        
        # now we built our bucket so we need to get the top most frequent elements
        res = []
        for bucket in range(len(buckets) - 1, -1, -1):
            for number in buckets[bucket]:
                res.append(number)
                if len(res) == k:
                    return res


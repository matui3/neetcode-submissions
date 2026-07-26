class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_bucket_list = [[] for i in range(len(nums) + 1)]
        result = []
        # get frequency of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 1 : 1, 2 : 2, 3 : 3
        # 7 : 2
        for key, value in count.items():
            freq_bucket_list[value].append(key)
        
        # the above SHOULD put the keys there
        
        for i in range(len(freq_bucket_list) - 1, 0, -1):
            for num in freq_bucket_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        


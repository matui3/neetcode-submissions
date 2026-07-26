class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        buckets = [[] for i in range(len(nums) + 1)]

        # count frequencies
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        
        for num, count in freq.items():
            buckets[count].append(num)
        
        answer = []
        for bucket in range(len(buckets) - 1, -1, -1):
            for number in buckets[bucket]:
                answer.append(number)
                if len(answer) == k:
                    return answer
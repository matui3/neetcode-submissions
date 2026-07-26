class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] # list of temps and idx

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prevTemp, prevIdx = stack.pop()
                result[prevIdx] = idx - prevIdx
            stack.append((temp, idx))
        
        return result
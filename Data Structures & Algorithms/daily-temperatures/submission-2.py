class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for index, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = index - prev_index
            stack.append(index)
        
        return answer
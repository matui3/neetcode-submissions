class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()

                wait_days = i - prev_index

                res[prev_index] = wait_days 

            stack.append(i)
        
        return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            # while we have stuff in the stack and while the current temp 
            # is greater than the top of the stack
            while stack and temp > stack[-1][0]:
                stackT, prevIdx = stack.pop()
                # the resulting temperature is going to be the current index minus the previous
                result[prevIdx] = idx - prevIdx

        
            stack.append((temp, idx))

        return result
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] < temp:
                result[stack[-1]] = i - stack[-1]
                stack.pop() 
            stack.append(i)
        return result
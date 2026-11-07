class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                result = max(result, (i - stack[-1][0])*stack[-1][1])
                start = stack[-1][0]
                stack.pop()
            stack.append([start, h])
        while stack:
            s, h = stack.pop()
            result = max((len(heights) - s)* h, result)
        return result
        
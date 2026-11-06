class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in closed:
                if not stack or stack[-1] != closed[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
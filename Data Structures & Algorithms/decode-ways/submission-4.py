class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        one = 1
        two = 0
        for index in range(n - 1, -1, -1):
            take1 = one if s[index] != "0" else 0
            if index + 1 < len(s) and "10"<=s[index: index + 2] <= "26":
                take2 = two
                cur = take2 + take1
            else:
                cur = take1
            two = one
            one = cur
        return one
    
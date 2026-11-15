class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [""]
        for i in range(len(s)):
            #even length for the palindrome substing
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(res[0]) < right - left - 1:
                res.pop()
                res.append(s[left + 1: right])
            


            #odd length for the palindrome substing
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(res[0]) < right - left - 1:
                res.pop()
                res.append(s[left + 1: right])
        return res[0]



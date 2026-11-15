class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            #even length for the palindrome substing
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if end - start + 1 < right - left - 1:
                start = left + 1
                end =  right - 1
            


            #odd length for the palindrome substing
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if end - start + 1 < right - left - 1:
                start = left + 1
                end =  right - 1
        return s[start : end + 1]



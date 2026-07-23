class Solution:
    def longestPalindrome(self, s):
        result = ""

        for i in range(len(s)):
            # Odd length palindrome (center is s[i])
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left:right + 1]
                left -= 1
                right += 1

            # Even length palindrome (center is between s[i] and s[i+1])
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left:right + 1]
                left -= 1
                right += 1

        return result
class Solution:
    def characterReplacement(self, s, k):
        count = {}               # frequency of each character in window
        left = 0
        max_freq = 0             # most frequent character count in window
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1    # add right char
            max_freq = max(max_freq, count[s[right]])        # update max frequency

            # If changes needed > k, shrink window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1       # remove left char
                left += 1                  # shrink from left

            result = max(result, right - left + 1)    # update best window

        return result
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # put nums in a set 

        num_set = set(nums)
        longest = 0

        # check if n-1 previous number exists

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest,length)
        
        return longest

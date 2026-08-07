class Solution:
    def hammingWeight(self, n):
        count = 0

        while n:
            count += n & 1    # add last bit (0 or 1)
            n >>= 1           # shift right, remove last bit

        return count
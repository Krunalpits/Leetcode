class Solution(object):
    def maxProduct(self, nums):
        result = max(nums)
        currMax = 1
        currMin = 1

        for n in nums:
            temp = currMax
            currMax = max(n* currMax, n* currMin, n)
            currMin = min(n* temp, n* currMin, n)

            result = max(result, currMax)

        return result
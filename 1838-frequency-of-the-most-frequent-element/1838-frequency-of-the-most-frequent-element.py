class Solution(object):
    def maxFrequency(self, nums, k):
        
        nums.sort()
        left = 0
        current_sum = 0
        result = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while nums[right] * (right - left +1) - current_sum > k :
                current_sum -= nums[left]
                left += 1
            
            result = max(result, right-left +1)
        return result
        
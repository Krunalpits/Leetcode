class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:       # skip duplicate i
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # skip duplicate j
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:   # skip dup
                            left += 1
                        while left < right and nums[right] == nums[right + 1]: # skip dup
                            right -= 1

                    elif total < target:
                        left += 1          # need bigger sum
                    else:
                        right -= 1         # need smaller sum

        return result
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()        # stores indices, front is always the max
        result = []

        for i in range(len(nums)):
            # Remove indices outside the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)     # add current index

            # Window is full, record the max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
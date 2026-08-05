class Solution:
    def merge(self, intervals):
        intervals.sort()                          # sort by start time
        result = [intervals[0]]                   # start with first interval

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:  # overlap?
                result[-1][1] = max(result[-1][1], intervals[i][1])  # merge
            else:
                result.append(intervals[i])       # no overlap, add it

        return result
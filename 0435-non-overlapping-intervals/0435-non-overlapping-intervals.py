class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])   # sort by END time
        count = 0
        prev_end = intervals[0][1]           # end of first interval

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:   # overlap
                count += 1                    # remove this one
            else:                             # no overlap
                prev_end = intervals[i][1]   # keep it, update end

        return count
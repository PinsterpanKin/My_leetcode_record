class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                count += 1
        return count
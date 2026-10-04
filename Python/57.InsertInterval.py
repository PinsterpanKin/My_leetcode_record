class MySolution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for current in intervals:
            if newInterval[0] <= current[1] and newInterval[1] >= current[0]:
                newInterval[0] = min(current[0], newInterval[0])
                newInterval[1] = max(current[1], newInterval[1])
            else:
                res.append(current)
            res.append(newInterval)
            res.sort(key = lambda x: x[0])
            return res

#Solution without extra sorting
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        i = 0
        n = len(intervals)

        # Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Add all remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

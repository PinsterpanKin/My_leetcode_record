import heapq
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        ends = []
        for start, end in intervals:
            if ends and ends[0] <= start:
                heapq.heappop(ends)
            heapq.heappush(ends, end)
        return len(ends)

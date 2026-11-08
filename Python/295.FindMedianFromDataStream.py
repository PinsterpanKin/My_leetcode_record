class Solution:
    import heapq

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    
    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2
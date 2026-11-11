class MySolution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        count = sorted(count, key = count.get, reverse = True)
        return count[:k]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        frequency = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            frequency[freq].append(num)
        res = []
        for freq in range(len(nums), 0, -1):
            for num in frequency[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
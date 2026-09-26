class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start, path):
            res.append(path)
            for i in range(start, n):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return res
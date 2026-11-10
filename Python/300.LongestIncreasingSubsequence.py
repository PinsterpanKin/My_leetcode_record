class MySolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# O(n log n) solution using binary search
# We don't have to keep a correct sub, we just need to track a correct length
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if not sub or x > sub[-1]:
                sub.append(x)
            else:
                idx = bisect.bisect_left(sub, x)
                sub[idx] = x
        return len(sub)
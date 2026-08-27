class Solution:
    def canJump(self, nums: List[int]) -> bool:
        closest = len(nums) - 1
        for n in range(len(nums) - 2, -1, -1):
            if n + nums[n] >= closest:
                closest = n
        return closest == 0
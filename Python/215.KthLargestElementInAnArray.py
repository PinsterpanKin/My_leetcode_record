class GeneralSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = random.randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            i = left
            for j in range(left, right):
                if nums[j] < nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            if i < target:
                left = i + 1
            elif i > target:
                right = i - 1
            else:
                return nums[i]
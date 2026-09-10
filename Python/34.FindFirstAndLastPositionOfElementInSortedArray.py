class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        first, last = -1, -1
        
        # Find the first occurrence
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                first = mid
                right = mid - 1
        
        if first == -1:
            return [-1, -1]
        
        left, right = first, len(nums) - 1
        
        # Find the last occurrence
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                last = mid
                left = mid + 1
        
        return [first, last]

#Original solution: worst case O(n)
class OriginalSolution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        found = 0
        res = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                found = 1
                left, right = mid, mid
                break
        if found == 0:
            while left > 0 and nums[left - 1] == target:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            res[0], res[1] = left, right
        return res
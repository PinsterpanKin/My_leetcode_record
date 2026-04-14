""" 
In this problem, I applied the two-pointer technique to find the three numbers in the sorted array that sum closest to the target.
I initialized the closest_sum with the sum of the first three elements and then iterated through the array, adjusting the left and right pointers based on whether the current sum is less than or greater than the target. 
This approach ensures that we efficiently find the closest sum in O(n^2) time complexity.
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
"""
My original solution is correct and efficient in algorithm
However, I can further optimize the runtime by skipping duplicate elements for the left and right pointers as well.
Also, I can add a pruning step to break out of the loop early if the current sum is already greater than the target.
"""
def threeSumClosest(self, nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = nums[0] + nums[1] + nums[2]
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, n - 1

#pruning step
        min_sum = nums[i] + nums[left] + nums[left + 1]
        if min_sum > target:
            if abs(min_sum - target) < abs(closest_sum - target):
                closest_sum = min_sum
            if min_sum > target:
                break

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
    return closest_sum
"""
Following the solution for 15. 3Sum, we can extend the idea to solve 18. 4Sum.
The main idea is to sort the input array and use two nested loops to fix the first two numbers,
and then use two pointers to find the remaining two numbers that sum up to the target.

I am glad to solve this problem independently!
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()
        result = []
        
        for i in range(n - 3):
            # skip the duplicate value for i
            if i > 0 and nums[i - 1] == nums[i]:
                continue
                
            for j in range(i + 1, n - 2):
                # skip the duplicate value for j
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                
                prevalue = nums[i] + nums[j]
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = prevalue + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # move left and right pointers to the next different values to avoid duplicates in the result
                        left += 1
                        right -= 1
                        
                        # skip the duplicate values for left and right
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return result
# My solution: horrible time complexity O(2^n) but it works...
class Mysolution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robbing(i: int, curr_sum: int) -> int:
            if i >= len(nums):
                return curr_sum
            return max(robbing(i + 2, curr_sum + nums[i]), robbing(i + 3, curr_sum + nums[i]))
            
        return max(robbing(0, 0), robbing(1, 0))

class Solution:
    def rob(self, nums: list[int]) -> int:
        # rob1: max money until house i-2, rob2: max money until house i-1
        rob1, rob2 = 0, 0
        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2
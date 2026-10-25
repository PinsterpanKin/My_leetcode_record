class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(num, num * max_product)
            min_product = min(num, num * min_product)
            
            result = max(result, max_product)
        
        return result
class Solution:
    def twoSum(self,nums,target):
        hash={}
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [hash[target-nums[i]],i]
            hash[nums[i]]=i

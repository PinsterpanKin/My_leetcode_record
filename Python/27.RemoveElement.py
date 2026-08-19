class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        diff = 0
        for i in range(n):
            if nums[i]!=val:
                nums[diff]= nums[i]
                diff+=1
        return diff
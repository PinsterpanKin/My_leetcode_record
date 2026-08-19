class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i,j=0,1
        for j in range(n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
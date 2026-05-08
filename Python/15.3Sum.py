class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        nums.sort()
        result=[]
        if nums[0]>0 or nums[n-1]<0:
            return result
        
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            left=i+1
            right=n-1
            
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
                    
        return result
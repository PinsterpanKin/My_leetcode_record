class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        m = len(nums1)
        n = len(nums2)
        if m > n:
            #OOP--self, swap the input to make sure nums1 is the shorter one
            return self.findMedianSortedArrays(nums2, nums1)
        
        left = 0
        right = m
        halflen = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = halflen - i
            
            if i < right and nums2[j-1] > nums1[i]:
                left = i + 1
            elif i > left and nums1[i-1] > nums2[j]:
                right = i - 1
            else:
                maxleft = 0
                if i == 0:
                    maxleft = nums2[j-1]
                elif j == 0:
                    maxleft = nums1[i-1]
                else:
                    maxleft = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return maxleft
                
                minright = 0
                if i == m:
                    minright = nums2[j]
                elif j == n:
                    minright = nums1[i]
                else:
                    minright = min(nums1[i], nums2[j])
                #return type: float
                return (maxleft + minright) / 2.0
                
        return 0.0
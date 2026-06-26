#Translated from my original C code
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(s, left, right, n):
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1
        
        length=len(s)
        if length<=1: return s
        result_head=0
        max_length=0
        for i in range(length):
            len1=expand(s,i,i,length)
            len2=expand(s,i,i+1,length)
            temp=max(len1,len2)
            if temp>max_length:
                max_length=temp
                result_head=i-(temp-1)//2
        result=""
        for i in range(result_head,result_head+max_length):
            result+=s[i]
        return result
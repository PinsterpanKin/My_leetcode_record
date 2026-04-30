class Solution(object):
    def reverse(self, x):
        result=0
        is_negative= x<0
        if is_negative:
            x=-x
        while x!=0:
            digit=x%10
            x//=10
            result=result*10+digit
        if is_negative:
            result=-result
        if result>2**31-1 or result<-2**31:
            return 0
        return result
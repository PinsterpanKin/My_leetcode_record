#Beat 100% in time and 91% in space
class Solution(object):
    def myAtoi(self, s):
        n=len(s)
        i=0
        result=0
        sign=1
        while i<n and s[i]==" ":
            i+=1
        if i<n and (s[i]=="+" or s[i]=="-"):
            sign = 1 if s[i]=="+" else -1
            i+=1
        while i<n and s[i]>="0" and s[i]<="9":
            digit=int(s[i])
            result=10*result+digit
            i+=1
        result=sign*result
        if result>2**31-1:
            return 2**31-1
        if result<-2**31:
            return -2**31
        return result
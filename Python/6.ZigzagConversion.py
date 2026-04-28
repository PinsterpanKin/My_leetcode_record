#awaiting for improvement...
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n,k,T=len(s),0,2*numRows-2
        if numRows==1 or numRows>=n: return s
        result=''
        for row in range(0,numRows):
            for j in range(row,n,T):
                result+=s[j]
                if row>0 and row<numRows-1 and j+T-2*row<n:
                    result+=s[j+T-2*row]
        return result
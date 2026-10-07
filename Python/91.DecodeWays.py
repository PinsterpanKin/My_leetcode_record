#Never solved a dynamic programming problem so smoothly by myself, I believe that I am actually improving through practice. Proud!
class MySolution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if s[i-1] > "2" or s[i-1] == "0":
                    return 0
                elif i > 1:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 1
            else:
                if s[i-1] + s[i] > "26" or s[i-1] == "0":
                    dp[i] = dp[i-1]
                else:
                    if i > 1:
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = 2
        return dp[-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if "10" <= s[i-2:i] <= "26":
                dp[i] += dp[i-2]
        return dp[-1]
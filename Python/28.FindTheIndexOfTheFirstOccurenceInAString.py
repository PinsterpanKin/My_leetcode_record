class OriginalSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)
        for i in range(h_len - n_len + 1):
            j = 0
            while j < n_len and haystack[i + j] == needle[j]:
                j += 1
            if j == n_len:
                return i
            else:
                i += j
        return -1

class OptimizedSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        p_count = Counter(p)
        s_count = Counter()
        
        result = []
        p_length = len(p)
        
        for i in range(len(s)):
            s_count[s[i]] += 1
            
            if i >= p_length:
                if s_count[s[i - p_length]] == 1:
                    del s_count[s[i - p_length]]
                else:
                    s_count[s[i - p_length]] -= 1
            
            if s_count == p_count:
                result.append(i - p_length + 1)
        
        return result
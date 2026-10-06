class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        from collections import Counter as counter
        
        dict_t = counter(t)
        required = len(dict_t)
        
        left, right = 0, 0
        formed = 0
        window_counts = {}
        
        min_len, best_left, best_right = float("inf"), None, None
        
        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            while left <= right and formed == required:
                character = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_left = left
                    best_right = right
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_len == float("inf") else s[best_left:best_right + 1]
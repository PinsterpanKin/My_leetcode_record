def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    
    char_set = set()
    max_len = 0
    left = 0
    right = 0
    
    while right < n:
        if s[right] not in char_set:
            char_set.add(s[right])
            right += 1
            max_len = max(max_len, right - left)
        else:
            char_set.remove(s[left])
            left += 1
            
    return max_len
class Original_Solution:
    def lengthOfLastWord(self, s: str) -> int:
        current = len(s) - 1
        length = 0
        while current >= 0 and s[current] == ' ':
            current -= 1
        while current >= 0 and s[current] != ' ':
            length += 1
            current -= 1
        return length

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
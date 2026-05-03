# Still not effective enough...
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        dictionary={")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in dictionary:
                pop=stack.pop() if stack else "#"
                if dictionary[char]!=pop:
                    return False
            else:
                stack.append(char)
        return not stack
"""
This problem is an art of recursion tree
"""
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        dictionary = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            if index == len(digits):#when one path is complete by selecting combinations of letters
                result.append(path) #add the path to the result list
                return              #and return to previous layer of the recursion tree
            
            possible_letters = dictionary[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)#every time the program goes back here, the next path will use another letter
                path.pop()
        
        backtrack(0, [])#begining of the recursion tree
        return result
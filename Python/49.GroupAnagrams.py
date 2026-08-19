class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())
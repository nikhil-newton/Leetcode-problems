class Solution(object):
    def removeAnagrams(self, words):
        result = []
        for word in words :
            if result and sorted(word) == sorted(result[-1]):
                continue
            else:
                result.append(word)
        return result
"""
Runtime: 224 ms, faster than 54.79% of Python online submissions for Count the Number of Consistent Strings.
Memory Usage: 15.7 MB, less than 95.32% of Python online submissions for Count the Number of Consistent Strings.

"""


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        
        result = 0
        for i in words:
            res = 0
            for j in i:        
                if j in allowed:
                    res += 1
            if res == len(i):
                result += 1         

        return result
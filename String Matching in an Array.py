"""
case a:
Runtime: 32 ms, faster than 31.68% of Python online submissions for String Matching in an Array.
Memory Usage: 13.5 MB, less than 79.01% of Python online submissions for String Matching in an Array.

"""
class Solution(object):
    def stringMatching(self, words):
        
        result = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                elif words[i] in words[j]:
                    result.add(words[i])
        return list(result)


"""
case b:
Runtime: 28 ms, faster than 51.91% of Python online submissions for String Matching in an Array.
Memory Usage: 13.5 MB, less than 53.44% of Python online submissions for String Matching in an Array.
"""

class Solution(object):
    def stringMatching(self, words):
        
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i!=j:
                    result.append(words[i])
                    break
        return result
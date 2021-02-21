"""
case a:

Runtime: 24 ms, faster than 50.51% of Python online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.5 MB, less than 80.73% of Python online submissions for Check If Two String Arrays are Equivalent.

"""

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
             
        first = ""
        second = ""
        for i in range(len(word1)):
                first += word1[i]
                
        for j in range(len(word2)):
            second += word2[j]

        if first == second:
            return True

        else:
            return False

"""
Runtime: 16 ms, faster than 91.75% of Python online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.4 MB, less than 80.73% of Python online submissions for Check If Two String Arrays are Equivalent.

"""

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
             
        first = ""
        second = ""
        for i in word1:
                first += i
                
        for j in word2:
            second += j

        if first == second:
            return True

        else:
            return False


"""
case c:
Runtime: 24 ms, faster than 50.51% of Python online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.5 MB, less than 53.85% of Python online submissions for Check If Two String Arrays are Equivalent.

"""

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
             
        first = ""
        second = ""
        for i in word1:
                first += i
                
        for j in word2:
            second += j

        return first == second
            
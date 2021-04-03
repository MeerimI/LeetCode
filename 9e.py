"""
Runtime: 84 ms, faster than 10.22% of Python online submissions for Palindrome Number.
Memory Usage: 13.3 MB, less than 89.70% of Python online submissions for Palindrome Number.

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return  False
        elif str(x) == str(x)[::-1]:
            return True
        else: return False
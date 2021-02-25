"""
Runtime: 20 ms, faster than 46.72% of Python online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 13.3 MB, less than 91.94% of Python online submissions for Number of Steps to Reduce a Number to Zero.

"""

class Solution(object):
    def numberOfSteps (self, num):
                               
        result = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
                result += 1
            elif num % 2 == 1:
                num -= 1
                result += 1
            else: return 0
        return result


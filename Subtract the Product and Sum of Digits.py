"""
case a:
Runtime: 12 ms, faster than 92.83% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 13.3 MB, less than 92.57% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.

"""

class Solution(object):
    def subtractProductAndSum(self, n):
       
        mult = 1
        add = 0
        for i in str(n):
            mult *= int(i)
            add += int(i)
        return mult - add
         
            

"""
case b:
Runtime: 20 ms, faster than 44.17% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 13.2 MB, less than 99.49% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.

"""

class Solution(object):
    def subtractProductAndSum(self, n):
       
        mult = 1
        add = 0
        for i in str(n):
            mult *= int(i)
            add += int(i)
        return mult - add
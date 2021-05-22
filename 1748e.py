'''
Runtime: 20 ms, faster than 70.11% of Python online submissions for Sum of Unique Elements.
Memory Usage: 13.2 MB, less than 99.03% of Python online submissions for Sum of Unique Elements.
'''

class Solution(object):     # Сложность этого решения - O(n)
    def sumOfUnique(self, nums):
    
        sum = 0
        qtyOfDigits = {}
        for i in nums:             
            if i in qtyOfDigits:
                qtyOfDigits[i] += 1 
            else:
                qtyOfDigits[i] = 1
        for j in qtyOfDigits:
            if qtyOfDigits[j] == 1:
                sum += j
        return sum




'''
Runtime: 20 ms, faster than 70.11% of Python online submissions for Sum of Unique Elements.
Memory Usage: 13.3 MB, less than 66.56% of Python online submissions for Sum of Unique Elements.

'''

class Solution:         # Сложность этого решения - O(n)
    def sumOfUnique(self, nums):
        sum1 = 0
        for i in nums:
            if nums.count(i) == 1:
                sum1 = sum1 + i
        return sum1
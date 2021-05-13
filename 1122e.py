'''
Runtime: 32 ms, faster than 27.80% of Python online submissions for Relative Sort Array.
Memory Usage: 13.5 MB, less than 52.20% of Python online submissions for Relative Sort Array.
'''

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(arr2)):
            numberOfDigits  = arr1.count(arr2[i])
            while numberOfDigits > 0:
                res.append(arr2[i])
                arr1.remove(arr2[i])
                numberOfDigits -= 1
                
        return res + sorted(arr1)
            
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
            

'''
case b:

Runtime: 20 ms, faster than 92.41% of Python online submissions for Relative Sort Array.
Memory Usage: 13.5 MB, less than 51.22% of Python online submissions for Relative Sort Array.

'''

class Solution2(object):
    def relativeSortArray(self, arr1, arr2): 
        arr2_order = {n: i for i, n in enumerate(arr2)}    
        arr1_tuples = [(arr2_order.get(i, len(arr2_order)), i) for i in arr1]  
        t = sorted(arr1_tuples)     
        return [v for k,v in t]    
        
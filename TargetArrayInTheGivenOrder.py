"""
Runtime: 24 ms, faster than 44.53% of Python online submissions for Create Target Array in the Given Order.
Memory Usage: 13.4 MB, less than 70.55% of Python online submissions for Create Target Array in the Given Order.

"""

class Solution(object):
    def createTargetArray(self, nums, index):
                     
        result = []
        for i in range(len(nums)): result.insert(index[i], nums[i])
        return result
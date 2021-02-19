"""

Runtime: 28 ms, faster than 21.94% of Python online submissions for Number of Good Pairs.
Memory Usage: 13.3 MB, less than 71.12% of Python online submissions for Number of Good Pairs.


"""

class Solution(object):
    def numIdenticalPairs(self, nums):
       
        result = 0
        for i in range(len(nums)):
            if 1 <= len(nums) <= 100 and 1 <= nums[i] <= 100:
                for j in range(1, len(nums)):
                    if nums[i] == nums[j] and i < j:
                        result += 1
        return result
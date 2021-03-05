"""
Runtime: 484 ms, faster than 12.83% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 13.3 MB, less than 98.72% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.

"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
       
        result = []
        for i in range(len(nums)):
            counter = 0
            if 2 <= len(nums) <= 500 and 0 <= nums[i] <= 100:
                for j in range(len(nums)):
                    if j != i and nums[j] < nums[i]:
                        counter += 1
                result.append(counter)
        return result


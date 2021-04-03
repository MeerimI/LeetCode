"""
Runtime: 40 ms, faster than 25.40% of Python online submissions for Search Insert Position.
Memory Usage: 14 MB, less than 96.45% of Python online submissions for Search Insert Position.

"""

class Solution(object):
    def searchInsert(self, nums, target):
       
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    return nums.index(nums[i])
                elif nums[-1] < target:
                    return nums.index(nums[-1]) + 1
                else:  continue
                 
            

"""
Runtime: 32 ms, faster than 82.66% of Python online submissions for Search Insert Position.
Memory Usage: 14.1 MB, less than 53.45% of Python online submissions for Search Insert Position.
"""



class Solution2(object):
    def searchInsert(self, nums, target):
       
        if target not in nums:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)
        else:
            return nums.index(target)
            
     
            
            
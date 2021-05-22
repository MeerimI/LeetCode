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
            
     
            
            
'''
Runtime: 24 ms, faster than 99.65% of Python online submissions for Search Insert Position.
Memory Usage: 14.1 MB, less than 54.08% of Python online submissions for Search Insert Position.
'''

class Solution3(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= target:
                r = mid - 1
            elif nums[mid] <= target:
                l = mid + 1
        return l            
                
class Solution(object):
    def runningSum(self, nums):    
        d = []
        for i in range(len(nums)):
            if 1 <= len(nums) <= 1000 and -10 ** 6 <= nums[i] <= 10 ** 6:
                d.append(sum(nums[i::-1]))
        return d   
class Solution(object):
    def shuffle(self, nums, n):
           
        x = nums[:n]
        y = nums[n:]
        xy = []
        for i in range(len(nums)//2):
            if 1 <= n <= 500 and len(nums) == 2*n and 1 <= nums[i] <= 10 ** 3:
                xy.append(x[i])
                xy.append(y[i])
        return xy

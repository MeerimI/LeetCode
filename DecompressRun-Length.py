"""
case a:

Runtime: 64 ms, faster than 18.87% of Python online submissions for Decompress Run-Length Encoded List.
Memory Usage: 13.9 MB, less than 23.03% of Python online submissions for Decompress Run-Length Encoded List.

"""

class Solution(object):
    def decompressRLElist(self, nums):
               
        result = []
        m = {}
        for i in range(0, len(nums), 2): 
            a = i + 1
            m[nums[i]] = nums[a]
            while nums[i] > 0:
                result.append(nums[a])
                nums[i] -= 1

        return result




"""
case b:

Runtime: 60 ms, faster than 34.81% of Python online submissions for Decompress Run-Length Encoded List.
Memory Usage: 13.8 MB, less than 79.19% of Python online submissions for Decompress Run-Length Encoded List.

"""


class Solution(object):
    def decompressRLElist(self, nums):
               
        result = []
        first = []
        second = []
        for i in range(0, len(nums), 2):
            first.append(nums[i])

        for j in range(1, len(nums), 2):
            second.append(nums[j])  

        for j in range(len(first)):
            while first[j] > 0:
                result.append(second[j])
                first[j] -= 1

        return result



"""
case c:

Runtime: 68 ms, faster than 10.72% of Python online submissions for Decompress Run-Length Encoded List.
Memory Usage: 13.7 MB, less than 79.19% of Python online submissions for Decompress Run-Length Encoded List.

"""

class Solution(object):
    def decompressRLElist(self, nums):
               
        result = []
        freq = nums[::2]
        val = nums[1::2]
        for i in range(len(freq)):
            while freq[i] > 0:
                result.append(val[i])
                freq[i] -= 1
        return result






"""
case d:

Runtime: 52 ms, faster than 81.84% of Python online submissions for Decompress Run-Length Encoded List.
Memory Usage: 13.8 MB, less than 51.90% of Python online submissions for Decompress Run-Length Encoded List.

"""


class Solution(object):
    def decompressRLElist(self, nums):
               
        result = []       
        for i in range(0, len(nums)-1, 2):
            result +=  nums[i] * [nums[i+1]]
        return result
"""
Runtime: 64 ms, faster than 67.78% of Python online submissions for Sort Array By Parity.
Memory Usage: 14.5 MB, less than 21.46% of Python online submissions for Sort Array By Parity

"""

class Solution(object):
    def sortArrayByParity(self, A):
          
        result = []
        end = []
        for i in A:
            if i % 2 == 0:
                result.append(i)
            else: end.append(i)

        result.extend(end)
        return result


"""
Runtime: 108 ms, faster than 8.39% of Python online submissions for Sort Array By Parity.
Memory Usage: 14.2 MB, less than 76.56% of Python online submissions for Sort Array By Parity.

"""

class Solution(object):
    def sortArrayByParity(self, A):
        
        c = 0
        for i in range(len(A)):
            if A[i] %2  == 0:
                A[c], A[i] = A[i], A[c]
                c += 1
        return A
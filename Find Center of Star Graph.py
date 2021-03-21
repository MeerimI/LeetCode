"""
Runtime: 656 ms, faster than 100.00% of Python online submissions for Find Center of Star Graph.
Memory Usage: 52.4 MB, less than 100.00% of Python online submissions for Find Center of Star Graph.

"""

class Solution(object):
    def findCenter(self, edges):
        count = 1
        result = edges[0][0]
        for i in range(1, len(edges)):
            if result not in edges[i]:
                result = edges[0][1]
                count += 1       
            else: count += 1

        if count == len(edges): return result

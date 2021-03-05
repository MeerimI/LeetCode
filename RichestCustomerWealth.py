"""
case a:

Runtime: 396 ms, faster than 5.73% of Python online submissions for Richest Customer Wealth.
Memory Usage: 13.6 MB, less than 24.52% of Python online submissions for Richest Customer Wealth.

"""

class Solution(object):
    def maximumWealth(self, accounts):
        total = []
        result = 0
        for i in range(len(accounts)):
            sum = 0
            if len(accounts[i]) <= 50:
                for j in accounts[i]:
                    if 1 <= j <= 100:
                        sum += j    
                        total.append(sum)
                        for m in total:
                            if m > result:
                                result = m
        return result





"""
case b:
Runtime: 32 ms, faster than 95.52% of Python online submissions for Richest Customer Wealth.
Memory Usage: 13.4 MB, less than 53.00% of Python online submissions for Richest Customer Wealth.

"""

class Solution(object):
    def maximumWealth(self, accounts):
        result = []
        for i in range(len(accounts)):
            sum = 0
            if len(accounts[i]) <= 50:
                for j in accounts[i]:
                    if 1 <= j <= 100:
                        sum += j    
                        result.append(sum)
                        
        return max(result)
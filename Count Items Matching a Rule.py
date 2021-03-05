"""
Runtime: 212 ms, faster than 100.00% of Python online submissions for Count Items Matching a Rule.
Memory Usage: 20.9 MB, less than 100.00% of Python online submissions for Count Items Matching a Rule.

"""

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        
        result = 0

        if ruleKey == "type":
            for i in items:
                ruleKey = i[0]
                if ruleKey == ruleValue:
                    result += 1

        elif ruleKey == "color":
            for i in items:
                ruleKey = i[1]
                if ruleKey == ruleValue:
                    result += 1
        elif ruleKey == "name":
            for i in items:
                ruleKey = i[2]
                if ruleKey == ruleValue:
                    result += 1
        return result
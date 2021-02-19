"""
Runtime: 20 ms, faster than 42.64% of Python online submissions for Defanging an IP Address.
Memory Usage: 13.5 MB, less than 34.51% of Python online submissions for Defanging an IP Address.

"""

class Solution(object):
    def defangIPaddr(self, address):
        
        return address.replace(".", "[.]")
"""
Runtime: 16 ms, faster than 76.36% of Python online submissions for Goal Parser Interpretation.
Memory Usage: 13.4 MB, less than 63.76% of Python online submissions for Goal Parser Interpretation.

"""

class Solution(object):
    def interpret(self, command):       
        command = command.replace("(al)", "al")
        return command.replace("()", "o")
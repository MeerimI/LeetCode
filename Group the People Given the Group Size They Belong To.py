"""
Runtime: 64 ms, faster than 54.76% of Python online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 13.6 MB, less than 74.93% of Python online submissions for Group the People Given the Group Size They Belong To.

"""

class Solution(object):
    def groupThePeople(self, groupSizes):
                       
        result = []
        groups = {}
        for i, groupSize in enumerate(groupSizes):
            if groupSize in groups:
                if len(groups[groupSize][-1]) < groupSize:
                    groups[groupSize][-1].append(i)
                else:
                    groups[groupSize].append([i])

            else:
                groups[groupSize] = [[i]]
            
        for groupOfGroups in groups.values():
            for group in groupOfGroups:
                result.append(group)

        return result
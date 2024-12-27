class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for i in range(left, right+1):
            covered = False
            for j in ranges:
                if i in range(j[0], j[1]+1):
                    covered = True
                    break
            if not covered:
                return False
        return True

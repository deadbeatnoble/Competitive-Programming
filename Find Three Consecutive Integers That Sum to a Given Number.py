class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if (num + 3) % 3:
            return []
        n = (num+3)/3
        return [n-2, n-1, n]

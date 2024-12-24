class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n % 3 > 1:
                return False
            n //= 3
        return True
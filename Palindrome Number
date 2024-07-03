class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = x
        rev = 0

        while x > 0:
            d = x % 10
            rev = rev * 10 + d
            x = (x - d) / 10

        return y == rev

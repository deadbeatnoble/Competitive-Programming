class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        repeated = {}
        length = 0
        start = 0

        for curr in range(len(s)):
            if s[curr] in repeated and repeated[s[curr]] >= start:
                start = repeated[s[curr]] + 1
            repeated[s[curr]] = curr
            length = max(length, curr - start +1)
        return length

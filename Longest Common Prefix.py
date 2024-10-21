class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minlen = min(len(x) for x in strs)

        for i in range(minlen):
            if not all(s[i] == strs[0][i] for s in strs):
                return strs[0][:i]
        return strs[0][:minlen]

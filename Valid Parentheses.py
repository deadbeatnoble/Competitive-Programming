class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {")":"(","]":"[","}":"{"}
        for c in s:
            if c not in map:
                stack.append(c)
            else:
                top = stack.pop() if stack else "#"
                if top != map[c]:
                    return False
        return not stack

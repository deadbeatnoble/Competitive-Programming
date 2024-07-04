class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        prev = 0
        
        for x in s:
            if rom[x] > prev:
                result += rom[x] - 2 * prev
            else:
                result += rom[x]
            prev = rom[x]


        return result

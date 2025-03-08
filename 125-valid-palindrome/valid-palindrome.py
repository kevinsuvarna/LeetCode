class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = ""
        for el in s:
            if el.isalnum():
                new_s += el

        return new_s == new_s[::-1]
        
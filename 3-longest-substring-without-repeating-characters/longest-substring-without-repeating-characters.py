class Solution(object):
    def updateString(self, s, ch):
        mod_str = s[s.find(ch)+1:]
        return mod_str
        
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr = 0
        max_ctr = 0
        substr = ""
        for el in s:
            if el not in substr:
                ctr += 1
                substr += el
            else:
                if ctr > max_ctr:
                    max_ctr = ctr
                substr = self.updateString(substr, el) + el
                ctr = len(substr)
        if ctr > max_ctr:
            max_ctr = ctr
        return max_ctr
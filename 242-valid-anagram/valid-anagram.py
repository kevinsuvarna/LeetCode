class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_letters = {}
        for el in s:
            if el not in dict_letters:
                dict_letters[el] = 1
            else:
                dict_letters[el] += 1

        dict_letters1 = {}
        for el in t:
            if el not in dict_letters1:
                dict_letters1[el] = 1
            else:
                dict_letters1[el] += 1

        if len(dict_letters1) > len(dict_letters):
            dict_letters, dict_letters1 = dict_letters1, dict_letters

        
        for key in dict_letters:  
            if key not in dict_letters1:
                return False
            if dict_letters[key] != dict_letters1[key]:
                return False

        return True
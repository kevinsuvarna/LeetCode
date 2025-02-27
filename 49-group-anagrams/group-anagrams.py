class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = []
        for s in strs:
            sorted_strs.append(sorted(s))
        groups = {}

        # Iterate with enumerate to get both the sublist and its index
        for idx, sublist in enumerate(sorted_strs):
            # Convert list to tuple to use as a dictionary key
            key = tuple(sublist)

            # Add index to existing group or create a new one
            if key in groups:
                groups[key].append(idx)
            else:
                groups[key] = [idx]

        final_ans = []
        for key in groups:
            small_list = []
            for el in groups[key]:
                small_list.append(strs[el])
            final_ans.append(small_list)

        return final_ans
        
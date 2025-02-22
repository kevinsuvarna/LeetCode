class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}  # Empty dictionary to track encountered elements

        for num in nums:
            if num in seen:
                # print(f"{num} is a duplicate")
                return True
            else:
                seen[num] = True  # Mark as encountered
        return False
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m = len(nums1)
        n = len(nums2) 
        left = 0
        right = m
        median = 0
        
        while left <= right:
            part1 = (left + right) // 2
            part2 = (m + n + 1) // 2 - part1
            
            max_left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            min_right1 = float('inf') if part1 == m else nums1[part1]
            max_left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            min_right2 = float('inf') if part2 == n else nums2[part2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) %2 == 1:
                    median = max(max_left1, max_left2)
                else:
                    median = (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                break

            if max_left1 > min_right2:
                right = part1 - 1
            else:
                left = part1 + 1


        return median
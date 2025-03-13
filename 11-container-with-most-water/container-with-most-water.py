class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        if len(height) == 2:
            return min(height[0], height[1])
        max_area = 0
        l = 0
        r = len(height) - 1
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = min(height[i], height[j]) * (j-i)
        #         if area > max_area:
        #             max_area = area
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
            
        
        return max_area
        
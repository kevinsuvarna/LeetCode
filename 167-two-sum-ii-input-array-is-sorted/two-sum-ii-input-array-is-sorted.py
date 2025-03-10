class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lptr = 0
        rptr = len(numbers) - 1
        sum = numbers[lptr] + numbers[rptr]
        while sum != target:
            if sum < target:
                lptr += 1
                sum = numbers[lptr] + numbers[rptr]
            else:
                rptr -= 1
                sum = numbers[lptr] + numbers[rptr]

        return [lptr + 1, rptr + 1]
    
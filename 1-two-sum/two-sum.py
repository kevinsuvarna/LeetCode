class IndexTracker:
    def __init__(self, array, target):
        """
        Initialize with array and target value to track
        
        Parameters:
        array (list): The list to search in
        target: The value to find occurrences of
        """
        self.array = array
        self.target = target
        self.last_found_index = -1
        self.all_indices = [i for i, x in enumerate(array) if x == target]
        self.current_occurrence = 0
        
    def next_occurrence(self):
        """
        Returns the index of the next occurrence of target value
        Returns None if no more occurrences exist
        """
        if self.current_occurrence >= len(self.all_indices):
            return -1
            
        next_index = self.all_indices[self.current_occurrence]
        self.current_occurrence += 1
        self.last_found_index = next_index
        return next_index
        
    def has_more_occurrences(self):
        """Returns True if there are more occurrences to find"""
        return self.current_occurrence < len(self.all_indices)
        
    def total_occurrences(self):
        """Returns the total number of occurrences of the target value"""
        return len(self.all_indices)
        
    def reset(self):
        """Resets the tracker to start from the beginning"""
        self.current_occurrence = 0
        self.last_found_index = -1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        i = 0
        j = len(sorted_nums) - 1
        sum = sorted_nums[i] + sorted_nums[j]
        while(sum!=target):
            if sum > target:
                j -= 1
            else:
                i += 1
            sum = sorted_nums[i] + sorted_nums[j]
            if i > j:
                break
        num1 = sorted_nums[i]
        num2 = sorted_nums[j]
        if num1 != num2:
            return [nums.index(num1), nums.index(num2)]
        
        temp_ans = [num1, num2]
        ans = []
        for number in temp_ans:
            tracker = IndexTracker(nums, number)

            # Get first occurrence
            first_index = tracker.next_occurrence()  # Returns 1

            # Get second occurrence
            second_index = tracker.next_occurrence()  # Returns 4

        
            return [first_index, second_index]
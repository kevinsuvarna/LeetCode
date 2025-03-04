class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}
        freq_dict[nums[0]] = 1
        max_freq = 0
        for i in range(1, len(nums)):
            if nums[i] in freq_dict:
                freq_dict[nums[i]] += 1
            else:
                freq_dict[nums[i]] = 1
                
        for val in freq_dict:
            if freq_dict[val] > max_freq:
                max_freq = freq_dict[val]

        arr = ['a'] * (max_freq + 1)
        for key in freq_dict:
            if isinstance(arr[freq_dict[key]], list):
                arr[freq_dict[key]].append(key)
            elif arr[freq_dict[key]] == 'a':
                arr[freq_dict[key]] = key
            else:
                arr2 = [arr[freq_dict[key]], key]
                arr[freq_dict[key]] = arr2
        ans = []
        
        for i in range(len(arr)-1, 0, -1):
            if k == 0:
                break
            if arr[i] == 'a':
                continue
            elif isinstance(arr[i], list):
                for j in arr[i]:
                    ans.append(j)
                    k -= 1
                    if k == 0:
                        break
            else:
                ans.append(arr[i])
                k -= 1
        return ans
    
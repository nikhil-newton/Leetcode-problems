class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter 
        counts = Counter(nums)
        return list(num for num in counts if counts[num] > len(nums)/3)
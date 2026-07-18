class Solution(object):
    def containsDuplicate(self, nums):
        s = set(nums)
        return True if len(nums) != len(s) else False
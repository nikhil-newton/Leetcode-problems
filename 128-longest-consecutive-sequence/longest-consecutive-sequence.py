class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)

        longest = 0

        for num in s:
            if num - 1 not in s:

                length = 1
                current = num

                while current + 1 in s:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
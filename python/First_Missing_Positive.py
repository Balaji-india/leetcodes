class Solution(object):
    def firstMissingPositive(self, nums):
        nums.sort()
        i = 1
        for num in nums:
            if num == i:
                i += 1
        return i

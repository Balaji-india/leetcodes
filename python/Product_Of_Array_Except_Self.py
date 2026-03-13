class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        pref = 1
        for i in range(n):
            answer[i] = pref
            pref *= nums[i]
        suff = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suff
            suff *= nums[i]
        return answer

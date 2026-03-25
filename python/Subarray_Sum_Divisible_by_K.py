class Solution(object):
    def subarraysDivByK(self, nums, k):
        mp={0:1}
        count=0
        prefix_sum=0
        for num in nums:
            prefix_sum+=num
            rem=prefix_sum%k
            if rem<0:
                rem+=k
            if rem in mp:
                count+=mp[rem]
            mp[rem]=mp.get(rem,0)+1
        return count

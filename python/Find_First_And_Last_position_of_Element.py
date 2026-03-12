class Solution(object):
    def searchRange(self, nums, target):
        def findleft():
            left,right=0,len(nums)-1
            a=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    a=mid
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return a
        def findright():
            left,right=0,len(nums)-1
            a=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    a=mid
                    left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return a
        return [findleft(),findright()]

        

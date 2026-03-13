class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max1 = 0
        while left < right:
            current = min(height[left], height[right]) * (right - left)
            max1 = max(max1, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max1

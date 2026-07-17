class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        marea = 0

        while left < right :
            width = right - left
            min_length = min(height[left], height[right])
            area = width * min_length
            
            if area > marea :
                marea = area
            if height[left] < height[right] :
                left += 1
            else:
                right -= 1
        
        return marea
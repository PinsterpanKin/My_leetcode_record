class Solution(object):
    def maxArea(self, height):
        n = len(height)
        max_volume = 0
        left, right = 0, n - 1
        
        while left < right:
            current = min(height[left], height[right]) * (right - left)
            
            if current > max_volume:
                max_volume = current
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_volume
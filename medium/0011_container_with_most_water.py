class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0

        L = 0
        R = len(height) - 1
        
        while L < R :
            area = (R - L) * min(height[L], height[R])
            max_area = max(max_area, area)
            if height[L] <= height[R] :
                L += 1
            else :
                R -= 1

        return max_area
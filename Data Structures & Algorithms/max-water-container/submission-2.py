class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_amount = 0

        while left < right:
            current_height = min(heights[left], heights[right])
            current_amount = (right - left) * current_height

            max_amount = max(max_amount, current_amount)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_amount

        
            
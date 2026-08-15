class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        
        curr_height = 0
        max_amount = 0

        while left < right:
            curr_height = min(heights[left], heights[right])
            max_amount = max(max_amount, (right - left) * curr_height)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_amount
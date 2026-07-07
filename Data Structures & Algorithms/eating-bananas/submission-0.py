class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            left = 1
            right = max(piles)

            ans = 0

            while left <= right:
                mid_speed = (left + right) // 2
                total_hours = 0

                for banana in piles:
                    total_hours += math.ceil(banana / mid_speed)

                if total_hours <= h:
                    right = mid_speed - 1
                    ans = mid_speed
                else:
                    left = mid_speed + 1
            return ans

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        matrix_size = m * n
        left = 0 
        right = matrix_size - 1

        while left <= right:
            mid = (left + right) // 2

            rows = mid // n
            cols = mid % n 

            curr_val = matrix[rows][cols]

            if curr_val == target:
                return True
            elif curr_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
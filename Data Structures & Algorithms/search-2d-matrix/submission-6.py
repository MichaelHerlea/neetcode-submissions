class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len, col_len = len(matrix), len(matrix[0])
        left, right = 0, row_len * col_len - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // col_len][mid % col_len]

            if value == target: return True
            if value < target:
                left = mid + 1
            else: # value > target
                right = mid - 1

        return False




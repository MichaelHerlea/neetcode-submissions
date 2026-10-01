class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        first_row = 1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row != 0:
                        matrix[row][0] = 0
                    else:
                        first_row = 0
        
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
        
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        
        if first_row == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
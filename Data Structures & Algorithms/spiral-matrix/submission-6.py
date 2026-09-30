class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        x_index, y_index, state = 0, 0, 0
        #state def: 0=right, 1=down, 2=left, 3=up

        if len(matrix[0]) == 1:
            return [row[0] for row in matrix]

        for _ in range((bottom + 1) * (right + 1)):
            output.append(matrix[y_index][x_index])
            if state == 0: x_index += 1
            elif state == 1: y_index += 1
            elif state == 2: x_index -= 1
            elif state == 3: y_index -= 1

            if state == 0 and x_index == right:
                state = (state + 1) % 4
                top += 1
            elif state == 1 and y_index == bottom:
                state = (state + 1) % 4
                right -= 1
            elif state == 2 and x_index == left:
                state = (state + 1) % 4
                bottom -= 1
            elif state == 3 and y_index == top:
                state = (state + 1) % 4
                left += 1

        return output
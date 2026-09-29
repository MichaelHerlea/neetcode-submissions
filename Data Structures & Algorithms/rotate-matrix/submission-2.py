class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        tracks = length // 2
        L, T = 0, 0
        R, B = length - 1, length - 1

        for track in range(tracks):
            local_length = length - 2 * track - 1
            for offset in range(local_length):
                temp_var = 0
                for i in range(4):
                    match i:
                        case 0:
                            temp_var = matrix[T][L + offset]
                            matrix[T][L + offset] = matrix[B - offset][L]
                        case 1:
                            matrix[B - offset][L] = matrix[B][R - offset]
                        case 2:
                            matrix[B][R - offset] = matrix[T + offset][R]
                        case 3:
                            matrix[T + offset][R] = temp_var
            L += 1
            T += 1
            R -= 1
            B -= 1

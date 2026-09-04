class Solution {
    public boolean isValidSudoku(char[][] board) {
        ArrayList<HashSet<Integer>> rows = new ArrayList<>();
        ArrayList<HashSet<Integer>> columns = new ArrayList<>();
        ArrayList<HashSet<Integer>> squares = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            rows.add(i, new HashSet<>());
            columns.add(i, new HashSet<>());
            squares.add(i, new HashSet<>());
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (rows.get(i).contains(board[i][j] - '0') ||
                        columns.get(j).contains(board[i][j] - '0') ||
                        squares.get((i / 3) + (j / 3) * 3).contains(board[i][j] - '0')) {
                            return false;
                    }
                    else {
                        rows.get(i).add(board[i][j] - '0');
                        columns.get(j).add(board[i][j] - '0');
                        squares.get((i / 3) + (j / 3) * 3).add(board[i][j] - '0');
                    }
                }
            }
        }

        return true;
    }
}

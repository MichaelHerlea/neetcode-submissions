class Solution {
    int rowLength;
    int colLength;
    String targetWord;
    boolean[][] path;
    char[][] board;

    public boolean exist(char[][] board, String word) {
        this.rowLength = board.length;
        this.colLength = board[0].length;
        this.targetWord = word;
        this.path = new boolean[rowLength][colLength];
        this.board = board;

        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < colLength; j++) {
                this.path = new boolean[rowLength][colLength];
                if (searchBox(i, j, 0)) return true;
            }
        }
        return false;
    }

    public boolean searchBox(int r, int c, int index) {
        if (index == targetWord.length()) return true;
        if (r < 0 || c < 0 ||
            r >= rowLength || c >= colLength ||
            path[r][c] == true ||
            targetWord.charAt(index) != board[r][c]) {
                return false;
            }
        path[r][c] = true;
        boolean result = searchBox(r + 1, c, index + 1) || 
            searchBox(r - 1, c, index + 1) ||
            searchBox(r, c + 1, index + 1) ||
            searchBox(r, c - 1, index + 1);
        path[r][c] = false;
        return result;
    }
}

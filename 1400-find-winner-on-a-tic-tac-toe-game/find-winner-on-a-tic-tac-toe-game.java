public class Solution {
    public String tictactoe(int[][] moves) {
        char[][] filled = new char[3][3];

        // A = 'X', B = 'O'; A is odd B is even
        for (int i = 0; i < moves.length; i++) {
            int row = moves[i][0];
            int col = moves[i][1];

            char player = (i % 2 == 0) ? 'X' : 'O';
            filled[row][col] = player;

            if (checkWinner(filled, row, col, player)) 
                return (player == 'X') ? "A" : "B";
        }
        return (moves.length == 9) ? "Draw" : "Pending";
    }

    private boolean checkWinner(char[][] filled, int row, int col, char player) {
        // Check row
        if (filled[row][0] == player && filled[row][1] == player && filled[row][2] == player)
            return true;

        // Check column
        if (filled[0][col] == player && filled[1][col] == player && filled[2][col] == player)
            return true;

        // Check main diagonal
        if (row == col && filled[0][0] == player && filled[1][1] == player && filled[2][2] == player)
            return true;

        // Check anti-diagonal
        if (row + col == 2 && filled[0][2] == player && filled[1][1] == player && filled[2][0] == player)
            return true;

        return false;
    }
}

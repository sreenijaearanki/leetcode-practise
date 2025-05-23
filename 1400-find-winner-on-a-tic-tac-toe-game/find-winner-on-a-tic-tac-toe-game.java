import java.io.*;
class Solution {
    public String tictactoe(int[][] moves) {
        int rows[] = new int[3];
        int cols[] = new int[3];
        int diag=0;
        int anti=0;

        int player=1; //A is 1; B is -1;

        for(int[] m:moves)
        {
            int r=m[0];
            int c=m[1];

            rows[r]=rows[r]+player;
            cols[c]=cols[c]+player;

            if(r==c)
            diag=diag+player;

            if(r+c==2)
            anti=anti+player;

        if (Math.abs(rows[r])==3||Math.abs(cols[c])==3||Math.abs(diag)==3||Math.abs(anti)==3)
        {
            if(player==1)
            return "A";
            else
            return "B";
        }

        player=player*-1;
        }

        if(moves.length==9)
        return "Draw";
        else
        return "Pending";
    }
}
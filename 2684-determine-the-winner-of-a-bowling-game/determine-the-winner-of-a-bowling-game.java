class Solution {
    public int isWinner(int[] player1, int[] player2) {
        int tot1=0,tot2=0;
        
        for(int i=0;i<player1.length;i++)
        {
            int score1=player1[i];
            int score2=player2[i];

            if((i>=1 && player1[i-1]==10) || (i>=2 && player1[i-2]==10))
            {
                score1 *= 2;
            }
            if((i>=1 && player2[i-1]==10) || (i>=2 && player2[i-2]==10))
            {
                score2 *= 2;
            }
            tot1+=score1;
            tot2+=score2;
        }

        if(tot1>tot2)
        return 1;
        else if(tot2>tot1)
        return 2;
        else
        return 0;
    }
}
class Solution {
    public String winningPlayer(int x, int y) {
        int p= Math.min(x,y/4);
        if(p%2==0)
        return "Bob";
        else
        return "Alice";
    }
}
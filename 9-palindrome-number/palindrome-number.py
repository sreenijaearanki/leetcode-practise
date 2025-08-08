class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        p=0
        num=x
        while num>0:
            p=(p*10)+(num%10)
            num//=10
            
        if p==x:
            return True
        else:
            return False
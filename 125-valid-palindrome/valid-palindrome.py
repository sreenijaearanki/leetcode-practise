class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(ch.lower() for ch in s if ch.isalnum())
        left=0
        right=len(string)-1

        while left<=right:  
            if string[left] != string[right]:
                return False
            left+=1
            right-=1
        return True


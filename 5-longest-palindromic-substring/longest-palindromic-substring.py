class Solution:
    def longestPalindrome(self, s: str) -> str:
         # Edge case: empty string or single character is always a palindrome
        if not s or len(s) == 1:
            return s

        start, end = 0, 0  # Tracks the start and end indices of the longest palindrome found

        # Loop through every index in the string
        for i in range(len(s)):
            # Try to expand around a single character (odd-length palindrome)
            len1 = self.expandFromCenter(s, i, i)

            # Try to expand around two characters (even-length palindrome)
            len2 = self.expandFromCenter(s, i, i + 1)

            # Get the maximum length from both cases
            max_len = max(len1, len2)

            # If the newly found palindrome is longer than the previous best
            if max_len > (end - start):
                # Recalculate start and end indices to capture this new palindrome
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return the longest palindromic substring using the final start and end
        return s[start:end + 1]

    def expandFromCenter(self, s: str, left: int, right: int) -> int:
        # Expand as long as left and right characters match and bounds are valid
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1  # Move left pointer outward
            right += 1  # Move right pointer outward

        # Length of the palindrome is right - left - 1
        return right - left - 1
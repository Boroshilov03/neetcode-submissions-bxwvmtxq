class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        # Initialize pointers for the start and end of the string
        left, right = 0, len(s) - 1
        
        # Compare characters from both ends towards the center
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

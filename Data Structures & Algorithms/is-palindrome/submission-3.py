class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for charac in s:
            if charac.isalnum():
                newStr += charac.lower()
        return newStr.lower() == newStr[::-1].lower()
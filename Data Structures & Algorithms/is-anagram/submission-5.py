class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count, t_char_count = dict(), dict()

        if not s or not t:
            return False

        if len(s) != len(t):
            return False
            
        n = len(s)
        for i in range(n):
            s_char_count[s[i]] = s_char_count.get(s[i], 0) + 1
            t_char_count[t[i]] = t_char_count.get(t[i], 0) + 1

        if s_char_count != t_char_count:
            return False

        return True
        
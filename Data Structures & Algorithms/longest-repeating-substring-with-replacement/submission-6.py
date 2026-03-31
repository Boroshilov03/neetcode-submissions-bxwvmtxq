class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        charMap = {}
        res= 0
        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            frequency = charMap[s[r]]
            maxf = max(frequency, maxf)
            while (r - l +1) - maxf > k:
                charMap[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
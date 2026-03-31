class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charCount = {}
        maxf = 0
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r],0 )
            maxf = max(maxf, charCount[s[r]])

            if (r-l-maxf+1) > k:
                charCount[s[l]]-= 1
                l+=1
            
        return r-l+1
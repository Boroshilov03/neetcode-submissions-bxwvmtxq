class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        countChar = {} # key (char) : value (count)
        maxf = 0
        res = 0
        for r in range(len(s)):
            countChar[s[r]] = 1 + countChar.get(s[r], 0)
            maxf = max(maxf, countChar[s[r]])
            if (r-l+1) - maxf > k:
                countChar[s[l]] -= 1
                l+=1
        return r-l+1

        # l = 0
        # charCount = {}
        # maxf = 0
        # for r in range(len(s)):
        #     charCount[s[r]] = 1 + charCount.get(s[r], 0)
        #     maxf = max(maxf, charCount[s[r]])
        
        #     if (r-l+1-maxf) > k:#if we more values than actual replacements
        #         charCount[s[l]] -=1
        #         l+=1

        # return (r-l+1)
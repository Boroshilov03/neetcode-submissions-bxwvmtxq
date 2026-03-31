from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count frequency of characters in t
        t_freq = Counter(t)
        window_freq = {}
        
        l = 0
        formed = 0
        required = len(t_freq)  # Number of unique characters in t
        min_len = float("inf")
        min_substr = ""

        for r in range(len(s)):
            # Add the rightmost character to the window
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1

            # If this character is in t and matches its required frequency
            if s[r] in t_freq and window_freq[s[r]] == t_freq[s[r]]:
                formed += 1

            # Try to shrink the window from the left
            while formed == required:
                curr_window = s[l:r + 1]
                if len(curr_window) < min_len:
                    min_len = len(curr_window)
                    min_substr = curr_window
                
                # Remove leftmost character from window
                window_freq[s[l]] -= 1
                if s[l] in t_freq and window_freq[s[l]] < t_freq[s[l]]:
                    formed -= 1
                
                l += 1  # Move left pointer

        return min_substr

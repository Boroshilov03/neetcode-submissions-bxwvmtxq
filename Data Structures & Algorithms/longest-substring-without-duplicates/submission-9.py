class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Left pointer
        l = 0
        # Store the last index of each character
        char_index = {}
        max_length = 0

        for r, char in enumerate(s):
            if char in char_index and char_index[char] >= l:
                # Move left pointer past the previous occurrence
                l = char_index[char] + 1

            # Update the last index of the character
            char_index[char] = r

            # Update max length
            max_length = max(max_length, r - l + 1)

        return max_length
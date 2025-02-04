class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_lenght = 0
        left = 0
        last_seen = {}

        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
            
            max_lenght = max(max_lenght, right-left+1)
            last_seen[c] = right
        return max_lenght
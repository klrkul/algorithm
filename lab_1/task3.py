class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        sub = []
        max_len = 0
        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.append(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
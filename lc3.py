#Longest substring without repeating characters

# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            length = (r-l)+1
            charSet.add(s[r])
            longest = max(length, longest)
        return longest
    

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))

        
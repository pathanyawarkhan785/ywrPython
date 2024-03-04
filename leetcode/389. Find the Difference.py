class Solution:
    def findTheDifference(self, s, t):
        temp = ""
        if len(s) < len(t):
            for i in range(0, len(s)):
                if s[i] in t:
                    temp += s[i]
                    s.replace(s[i], "")


newFindDifference = Solution()
newFindDifference.findTheDifference("abcd", "abcde")

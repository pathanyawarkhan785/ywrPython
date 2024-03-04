class Solution:
    def longestCommonPrefix(self, strs):

        strs.sort(key=len)
        temp = strs[0]
        newTemp = ""

        for j in range(1, len(strs)):
            for i in range(0, len(temp)):
                if temp[i] == strs[j][i]:
                    newTemp += temp[i]

            temp = ""
            temp = newTemp
            newTemp = ""

        return temp


newLongestCommon = Solution()
print(newLongestCommon.longestCommonPrefix(["flower", "flow", "floght", "flop"]))

# class Solution:
#     def longestCommonPrefix(self, strs):
#         commonPrefix = ""
#         strs = sorted(strs, key=len)
#         # print(strs)
#         for i in range(len(strs)):
#             for j in range(0, len(strs)):
#                 # print(j, i)
#                 if (
#                     j + 2 < len(strs)
#                     and strs[j][i] == strs[j + 1][i]
#                     and strs[j][i] == strs[j + 2][i]
#                 ):
#                     # print(strs[j][i])
#                     commonPrefix += strs[j][i]

#         return commonPrefix


# newStr = Solution()
# print(newStr.longestCommonPrefix(["flower", "flow", "flight"]))

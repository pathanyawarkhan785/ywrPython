class Solution:
    def isValid(self, s: str) -> bool:

        openBracks = "{(["
        closeBracks = "})]"

        myli = []
        myli2 = []

        for i in s:
            if i in openBracks:
                myli.append(i)
            else:
                myli2.append(i)

        if len(myli) == len(myli2):
            return "true"
        else:
            return "false"


newStr = Solution()
print(newStr.isValid("()"))

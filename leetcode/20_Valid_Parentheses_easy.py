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

        print("true") if (len(myli) == len(myli2)) else print("false")


newStr = Solution()
newStr.isValid("()")

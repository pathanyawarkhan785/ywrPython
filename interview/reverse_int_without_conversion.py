# # work for only positive input


class Solution:
    def reverse(self, x):
        elem = 0
        while 1:
            if x <= 0:
                return elem
            elem = elem * 10 + x % 10
            x = x // 10
            print(x)


newReverse = Solution()
print(newReverse.reverse(123))

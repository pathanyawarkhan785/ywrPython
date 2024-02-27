class Solution:
    def removeDuplicates(self, nums):

        nums = set(nums)
        return len(nums), list(nums)


newVal = Solution()
print(newVal.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

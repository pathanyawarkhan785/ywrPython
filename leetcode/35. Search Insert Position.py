nums = [1, 3, 5, 6]
target = 4


class Solution:
    def searchInsert(self, nums: str, target: str) -> int:
        if target in nums:
            return nums.index(target)
        for i in range(0, len(nums)):
            if nums[i] > target:
                nums.insert(i, target)
                return i


insPos = Solution()
print(insPos.searchInsert(nums, target))

nums = [1, 2, 3, 4]
target = 5


def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            # print(nums[i], nums[j])
            if nums[i] + nums[j] == target:
                return [nums.index(nums[i]), nums.index(nums[j], 2)]


print(twoSum(nums, target))

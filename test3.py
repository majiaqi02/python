def threeSum(nums):
    nums.sort()  # 先对数组进行排序
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复元素
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:  # 跳过重复元素
                    left += 1
                while left < right and nums[right] == nums[right - 1]:  # 跳过重复元素
                    right -= 1
                left += 1
                right -= 1
    return res


# 测试
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
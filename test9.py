def maximum_product(nums):
    # 对数组进行排序
    nums.sort()
    n = len(nums)

    # 获取最大的三个数的乘积
    max_three = nums[n - 1] * nums[n - 2] * nums[n - 3]

    # 如果数组长度大于3，检查使用两个最小负数（如果存在）和最大正数的乘积
    if n > 3 and nums[0] < 0 and nums[1] < 0:
        max_two_min_one_max = nums[0] * nums[1] * nums[n - 1]
        # 比较两种情况并返回较大的乘积
        return max(max_three, max_two_min_one_max)
    else:
        # 否则，只可能有一种情况（即最大的三个数）
        return max_three

    # 示例


nums = [-10, -10, 5, 2]
print(maximum_product(nums))  # 输出应该是 500，因为 -10 * -10 * 5 = 500

nums = [53, 53, 6, 7]
print(maximum_product(nums))
def twoSum(nums, target):
    # 创建一个字典来存储数组元素和它们的索引
    num_dict = {}

    # 遍历数组
    for i, num in enumerate(nums):
        # 计算目标值与当前值的差
        complement = target - num

        # 检查差是否已经在字典中
        if complement in num_dict:
            # 如果在，返回结果
            return [num_dict[complement], i]

            # 如果不在，将当前值及其索引添加到字典中
        num_dict[num] = i

        # 如果没有找到符合条件的两个数，返回空列表（或者抛出异常）
    return []


# 测试
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # 输出应该是 [0, 1]，因为 nums[0] + nums[1] = 2 + 7 = 9
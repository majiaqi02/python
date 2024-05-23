def average_of_numbers(*args):
    """
    计算任意个数字的平均值

    参数:
    *args -- 不定数量的数字参数

    返回:
    float -- 输入数字的平均值
    """
    if not args:  # 检查是否传入了任何参数
        raise ValueError("没有传入任何数字")
    return sum(args) / len(args)


# 使用示例
numbers = [1, 2, 3, 4, 5]
print(average_of_numbers(*numbers))  # 使用 * 来解包列表为单独的参数

# 或者直接传入数字作为参数
print(average_of_numbers(1, 2, 3, 4, 5))
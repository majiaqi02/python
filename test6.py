def plusOne(digits):
    # 从数组末尾开始
    carry = 1  # 初始进位为1
    i = len(digits) - 1

    # 遍历数组
    while i >= 0:
        # 加一并与进位相加
        sum_digit = digits[i] + carry

        # 更新当前位的值
        digits[i] = sum_digit % 10

        # 更新进位
        carry = sum_digit // 10

        # 向前移动一位
        i -= 1

        # 如果最高位还有进位，则在数组最前面插入1
    if carry:
        digits.insert(0, carry)

    return digits


# 示例用法
digits = [1, 2, 3]
print(plusOne(digits))  # 输出: [1, 2, 4]

digits = [9, 9, 9]
print(plusOne(digits))  # 输出: [1, 0, 0, 0]

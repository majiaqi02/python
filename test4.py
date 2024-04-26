def is_palindrome(num):
    # 将数转换为字符串
    str_num = str(num)
    # 检查字符串是否与其反转字符串相等
    return str_num == str_num[::-1]


# 测试函数
print(is_palindrome(121))  # 输出: True
print(is_palindrome(12321))  # 输出: True
print(is_palindrome(12345))  # 输出: False
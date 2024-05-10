def count_words(s):
    # 移除字符串两端的空格
    s = s.strip()

    # 如果字符串为空，则没有单词
    if not s:
        return 0

        # 使用split方法根据空格分割字符串，但这里我们需要处理连续的空格
    # 因此我们使用split()而不带任何参数，它默认按任意空白（空格、制表符、换行符等）分割
    words = s.split()

    # 返回分割后得到的单词列表的长度
    return len(words)


# 示例用法
s = "Hello,  world!  This is a test string.  "
print(count_words(s))  # 输出: 7
def lengthOfLongestSubstring(s):
    if not s:
        return 0

    hash_set = set()
    max_len = start = 0
    for end in range(len(s)):
        while s[end] in hash_set:
            hash_set.remove(s[start])
            start += 1
        hash_set.add(s[end])
        max_len = max(max_len, end - start + 1)
    return max_len


# 测试代码
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # 输出: 3，因为无重复字符的最长子串是 "abc"

# from openpyxl import load_workbook
#
# # 加载工作簿
# wb = load_workbook('attack.csv')
# # 选择活动工作表，或者通过名称选择其他工作表
# ws = wb['attack']
#
# # 假设我们想要检查第一列（索引为0）的文字
# unique_texts = set()
# for cell in ws['A']:  # 遍历A列的所有单元格
#     if cell.value is not None and isinstance(cell.value, str):  # 确保值存在且为字符串
#         unique_texts.add(cell.value)
#
#     # 打印不重复的文字
# print("不重复的文字:")
# for text in sorted(unique_texts):  # 对结果进行排序以便阅读（可选）
#     print(text)


# import csv
#
# # 假设CSV文件的第一列包含文字
# unique_texts = set()
#
# with open('attack.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     # 跳过标题行（如果有的话）
#     next(reader, None)
#     for row in reader:
#         # 假设文字在第一列
#         text = row[0]
#         if text and isinstance(text, str):
#             unique_texts.add(text)
#
#         # 打印不重复的文字
# print("不重复的文字:")
# for text in sorted(unique_texts):
#     print(text)


import csv
from collections import Counter

# 假设你的CSV文件名为'attack.csv'，并且第一列包含你想要收集的文字
with open('attack.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 跳过标题行（如果CSV文件有标题行的话）
    next(reader, None)

    # 收集所有文字并计数
    word_counts = Counter()
    for row in reader:
        if row[0] and isinstance(row[0], str):  # 确保第一列的值存在且为字符串
            word_counts[row[0]] += 1

            # 筛选出不重复的文字（即计数为1的文字）
    unique_texts = [word for word, count in word_counts.items() if count == 1]

    # 按字母顺序排序（如果需要降序排序，稍后进行）
    unique_texts.sort()

    # 如果你想要降序排序（例如，按字母顺序的降序）
    unique_texts.reverse()

    # 打印不重复且降序排序的文字
    print("不重复且降序排序的文字:")
    for text in unique_texts:
        print(text)
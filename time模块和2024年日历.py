# import time
#
# # 初始化数字
# num = 0
#
# # 无限循环，每秒打印一个数字
# while True:
#     print(num)
#     num += 1
#     time.sleep(1)  # 暂停一秒
#
# # 注意：上面的代码会无限循环，你可能需要通过Ctrl+C来停止它


import calendar

# 设置每周的起始日为星期日
calendar.setfirstweekday(calendar.SUNDAY)

# 遍历2024年的每个月
for month in range(1, 13):
    # 打印每个月的日历
    print(calendar.month(2024, month))
    print("\n" * 2)  # 添加一些空行以分隔月份

# 注意：上面的代码会一次性打印整年的日历，而不是每隔一段时间打印一个月
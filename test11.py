# def sum(*nums):
# #定义一个变量，来保存结果
# result=0
# #遍历元祖，并将元祖中的数进行累加
# for n in nums:
#     result += n
# print(result)
#
# sum(123,456,789,10,20,30,40)
# sum(10,20,30)
# sum(12,78,90,67)

def sum_of_numbers(*args):
    """
    计算任意个数字的和

    参数:
    *args -- 任意数量的数字

    返回:
    result -- 所有数字的和
    """
    result = 0
    for num in args:
        result += num
    return result


# 使用示例
print(sum_of_numbers(1, 2, 3, 4, 5))  # 输出: 15
print(sum_of_numbers(10, 20, 30))  # 输出: 60
# def fun1(x, y):
#     print("这是函数一")
#     sum_result = x + y  # 变量名改为 sum_result 以避免与内置函数 sum 冲突
#     return sum_result
#
#
# def fun2():
#     print("这是函数二")
#     result = fun1(2, 3)  # 调用 fun1 并传入参数值 2 和 3
#     print(result)  # 打印 fun1 的返回值
#
#
# fun2()
#
#
# def max(x,y):
#     return x if x > y else y
#
# def maxs(a,b,c,d):
#     res1 = max(a,b)
#     res2 = max(res1, c)
#     res3 = max(res2,d)
#     return res3
# print(maxs(5,2,420,299))
# def f1():
#     def f2():
#         def f3():
#             pass
#         print("---->f1")
#         f2()
#
#
# def max(x, y):
#     return x if x > y else y
#
#
# def maxs(a, b, c, d):  # 这里缺少了冒号 :
#     res1 = max(a, b)
#     res2 = max(res1, c)
#     res3 = max(res2, d)  # 这里缺少了逗号 ,
#     return res3
#
#
# print(maxs(5, 2, 420, 299))  # 这将输出420
#
#
# def f1():
#     def f2():
#         def f3():
#             pass
#
#         print("---->f2")  # 这里应该是f2而不是f1
#         # f2() 这个调用是多余的，因为f2就是当前的函数，并且它内部已经定义了f3但并未调用
#         # 如果你想要调用f3，你应该在这里调用它，但注意f3是在f2的作用域内
#         # 如果你想在f1中调用f2，并且f2中调用f3，你需要重新组织代码
#
#     # 这里是f1的作用域，你需要调用f2
#     f2()
#
#
# # 现在调用f1
# f1()
#
#
# def f1():
#     def f2():
#         def f3():
#             print("---->f3")
#
#         print("---->f2")
#         f3()  # 调用f3
#
#     f2()  # 调用f2
#
#
# f1()  # 调用f1
#
#
#
#
#  #            n的阶乘
#  # 定义一个递归函数factorial,用于计算给定数值的阶乘。
#  # 如果输入的数值“n"等于1，则认为阶乘是1，因此我们返回1.
#  # 否则，我们通过将当前数值n与factorial(n-1)的结果相乘来递归计算阶乘
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return  n * factorial(n-1)
# num = 9
# result = factorial(num)
# print(f"The factorial of (num) is :{result}")
#
#
# #猴子吃桃
# #第一天摘下若干个桃子，当即吃了一半，又多吃了一个，第二天将剩下的桃子吃掉一半，
# #又多吃一个，后面每天均是如此，到第n天想吃时，只剩下一个，计算猴子第一天共摘了多少个桃子
#
# n = int(input()) #输入任意n表示第n天时，剩下一个桃子
#
# def F(x):
#     if x==1:
#         return x #边界
#     else:
#         return(F(x-1)+1)*2 #递归函数
#     print(F(n)) #输出递归值
#
#
#
#
# n = int(input())  # 输入任意n表示第n天时，剩下一个桃子
#
# #以下是使用循环
# def calculate_peaches(days):
#     peaches = 1  # 第n天剩下的桃子数量
#     for _ in range(days):
#         peaches = (peaches + 1) * 2  # 反向模拟每天猴子吃桃子的过程
#     return peaches
#
#
# print(calculate_peaches(n))  # 输出第一天摘的桃子数量



#斐波那契数列
def fibonacci_with_memoization(n, m={}):
    if n in m:
        return m[n]
    elif n <= 0:
        return "输入错误，请输入一个正整数"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        m[n] = fibonacci_with_memoization(n - 1, m) + fibonacci_with_memoization(n - 2, m)
        return m[n]

    # 测试函数


print(fibonacci_with_memoization(11))  # 输出第11个斐波那契数



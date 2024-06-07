# f = open('python.txt','r',encoding="utf-8")
# #encoding的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
# f = open('python.txt')
# content = f.readlines()
# # ['hello world\n','abcdefg\n','aaa\n','bbb\n','ccc']
# print(content)
# #关闭文件
# f.close
#
#
#
#
# f = open('python.txt')
# content = f.readlines()
# print(f'第一行:{content}')
# content = f.readlines()
# print(f'第二行:{content}')
# #关闭文件
# f.close
#
# for line in open("python.txt","r"):
#     print(line)
# #每一个line临时变量，就记录了文件的一行数据
#
#
# with open("python.txt","r") as  f:
#     f.readlines()


def count_python_occurrences(file_path):
    try:
        with open('word.txt', 'r', encoding='utf-8') as file:  # 打开文件
            content = file.read()  # 读取文件内容
            content = content.lower()  # 转换为小写
            words = content.split()  # 拆分为单词
            count = words.count('python')  # 统计Python出现的次数
            return count
    except FileNotFoundError:
        print(f"文件 {'word.txt'} 未找到。")
        return 0
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return 0

    # 使用函数并打印结果


file_path = 'word.txt'  # 替换为你的文件路径
count = count_python_occurrences(file_path)
print(f"python在文件中出现了{count}次。")






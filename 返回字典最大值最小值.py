def func(*args):
    the_max=args[0]
    the_min = args[0]
    for i in args:
        if i>the_max:
            the_max=i
        elif i<the_min:
            the_min=i
    return{'max':the_max,'min':the_min}
res=func(1,20,3,40,5)
print(res)

def find_max_and_min(numbers):  
    if not numbers:  # 检查列表是否为空  
        return {}  # 如果为空，返回一个空字典  
      
    # 使用内置的min和max函数找到最小值和最大值  
    max_value = max(numbers)  
    min_value = min(numbers)  
      
    # 返回一个包含最小值和最大值的字典  
    return {"max": max_value, "min": min_value}  
  
# 示例用法  
numbers = [4, 2, 9, 7, 5, 1]  
result = find_max_and_min(numbers)  
print(result)  # 输出: {'max': 9, 'min': 1}

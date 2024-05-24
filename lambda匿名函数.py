def test_func(compute):
    result = compute(1,2)
    print(result)

def compute(x,y):
    return x + y
# 使用命名函数 compute 作为参数  
test_func(compute)

def test_func(compute):
    result = compute(1, 2)
    print(result)
# 使用 lambda 表达式作为参数 
test_func(lambda x, y: x + y)




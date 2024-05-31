#                    date类
#                  一、date对象构成
# 1.date对象由year年份、month月份以及day日期三部分构成：date（year，month，day)
# 2.通过year，month，day三个数据描述符可以进行访问
from datetime import datetime

a = datetime.today()
print(a)
print(a.year)
print(a.month)
print(a.day)



#比大小
from datetime import date  # 注意这里是从datetime模块中导入date类
a=date(2017, 3, 1)
b=date(2017, 3, 15)
print(a.__eq__(b))  # False，因为a和b不是同一天
print(a.__ge__(b))  # False，因为a不晚于b
print(a.__gt__(b))  # False，因为a不大于b
print(a.__le__(b))  # True，因为a早于或等于b
print(a.__lt__(b))  # True，因为a早于b
print(a.__ne__(b))  # True，因为a和b不是同一天
print(a.__sub__(b))
print(a.__rsub__(b))
print(a == b)  # False
print(a >= b)  # False
print(a > b)   # False
print(a <= b)  # True
print(a < b)   # True
print(a != b)  # True

from datetime import date
a=date(2017,3,22)
print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%y/%m/%d'))
print(a.__format__('%D'))
print(a.__format__('%d'))
print(a.__str__())

from datetime import time
a=time(12,20,30,899)
print(a)
print(a.__format__('%H:%M:%S'))


from datetime import *
d = date(2012,12,12)
print(d)

#昨天
d1 = d + timedelta(days=-1)
print(d1)
#明天
d2 = d + timedelta(days=1)
print(d2)

from datetime import *
dt = datetime(2012,12,12,23,59,59)
print(dt)
#昨天
dt1=dt+timedelta(days=-1)
print(dt1)
#明天
dt2=dt+timedelta(days=1)
print(dt2)
#上一个小时
dt3=dt+timedelta(hours=-1)
print(dt3)
#下一个小时
dt4=dt+timedelta(hours=1)
print(dt4)
#上一秒
dt5=dt+timedelta(seconds=-1)
print(dt5)
#下一秒
dt6=dt+timedelta(seconds=1)
print(dt6)

import time
from datetime import datetime

# 使用 time 模块的 time 函数来获取时间戳
a = time.time()
for x in range(100000):
    pass
b = time.time() - a
print(b)

# 打印三次 perf_counter 的值
print(time.perf_counter())
print(time.perf_counter())
print(time.perf_counter())

from datetime import *
import time  # 导入 time 模块以使用 time 函数和 perf_counter 函数

a = time.time()  # 使用 time 模块的 time 函数获取时间戳
for x in range(100000):
    pass
b = time.time() - a
print(b)

# 打印三次 perf_counter 的值
print(time.perf_counter())  # 使用 time 模块的 perf_counter 函数
print(time.perf_counter())
print(time.perf_counter())

print(time.gmtime())
print(time.localtime())
a = time.time()
time.localtime(a)

print(time.time())
print(time.ctime(time.time()))

a = time.strftime("%Y-%m-%d",time.gmtime())
print(a)

b = time.strftime("%Y-%m-%d %X")
print(b)

c = time.strftime("%x %X")
print(c)

# -*- coding:utf-8 -*-
age = 2
if age >= 18:
    print('you are so yang')
    print ('you are')
    print ('so yang')
elif age >= 6:
    print('simple')
else:
    print("你, 那个小孩")

century = input('Year:')
birth = int(century)#输入的内容是str类型
if birth > 2000:
    print('simple')
else:
    print('yang man')
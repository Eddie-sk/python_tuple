# -*- coding: utf-8 -*-
my_name = '这世界很酷！'
print(my_name)
strFormat = 'Hello,%s' % 'world'
print(strFormat)
print('Hi, %s, you have more than %d.' % ('test', 100000000))
print('Age : %s,Gender:%s' % (28, True))
format1 = 'Hello {0}, your age is {1:0.1f}'.format('tony', 10.12)
print (format1)
print ('{0:0.1f}'.format((82+29) / 2))
# print('中'.encode('utf-8'))
classmates = ['张三', '李四', '王二麻']
print(classmates, len(classmates), classmates[-1], classmates.insert(1, '吴冰'))
print(classmates, classmates.pop())
print(classmates)

#tuple元组, tuple初始化之后，内容不可修改，即：没有append(), insert()这种方法

#空元组
t = ()
print(t)
#不可变元组：元组中只包含一个元素，该元素为：1，此种方式初始化的元组为不可变元组
t = (1)
print(t)
#t[0] = 12 不可变元组中的元素初始化后不可改变

#可变元组，初始化元组时，定义元组中包含几个元素可用(n, )
t = (1, )
print(t)
t[0] = 10

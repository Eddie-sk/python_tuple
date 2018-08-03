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
#元组初始化后元素不可改变
t = (1, 2)
print(t)
#t[0] = 12 元组中的元素初始化后不可改变

#若元组中只包含一个元素，在初始化时需要在元素后加"," Eg:因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = (1, )
print(t)
#"可变的"元组，此处的可变不是元组中的元素改变，而是list中的元素改变
t = ('a', 'b', ['A', 'B'])
print(t)

t[2][1] = 'Hello'
print(t)



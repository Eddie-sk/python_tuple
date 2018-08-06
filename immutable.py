# -*- coding:utf-8 -*-
#str是不可变对象，而list是可变对象。
str1 = '张三疯'
print str1.replace('张', 'wu')
#虽然字符串有个relpace方法，内容也变了，但是变量str1的内容却未改变，大大的way？
#尝试把代码改为下面这样：
str2 = str1.replace('张', 'wu')

print str1
print 'str2:', str2
#str1是变量，而'张三疯'才是字符串对象。通常我们说str1的内容是'xxx'，其实，a本身是一个变量，它指向的内容才是'xxx'
#我们调用的replace方法实际上是作用在字符串'xxx'上的，并没有改变字符串'xxx'的内容，只是返回了一个新的字符串


a = ['zhang', 'san', 'feng']
a.sort()
print a

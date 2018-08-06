# -*- coding:utf-8 -*-
names = ['xcode',
         'android studio',
         'pycharm']
for name in names:
    print name

#整数序列 range(n),然后通过list()函数转换为list
for num in list(range(10)):#(0-9)
    print num

sum = 0
n = 100

while n > 0:
    sum = sum + n
    n = n - 1
print  sum
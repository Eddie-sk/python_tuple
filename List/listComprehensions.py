# -- coding: utf-8 --

#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(1, 11)：

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []

for x in range(11):
    L.append(x * x)

print L

#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：

L = [x * x for x in range(11)]
print L


#还可以使用两层循环，可以生成全排列：

print [m + n for m in 'ABC' for n in 'XYZ']

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

import os

print [directory for directory in os.listdir('.')]#os.listdir 可以列出文件和目录


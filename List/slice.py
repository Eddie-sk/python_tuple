# -- coding: utf-8 --


#取一个list或tuple的部分数据是非常常见的操作。比如，一个list如下
L = ['Michael', 'Sarah', 'Tracy', 'Bob']
#取前三个数据

sl = L[:3]
print sl

#python支持L[-1]取最后一个元素，也可以使用倒数切片，例如

last = L[-1:]
print last

L = range(100)

print L[10:40:5]#10到40个元素，每隔5个取一个

print L[::3]#所有元素，每隔3个取一个

print L[:] #复制一个list
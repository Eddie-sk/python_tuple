# -*- coding:utf-8 -*-
#set无序的，在set中key不能重复
#要创建一个set，需要提供一个list作为输入集合：
s = set([1, 4, 3])
print s
s.add(2)
print s
s.remove(1)
print s

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 3, 5, 7, 8, 9])
s2 = set([2, 4, 6, 8, 10])

print s1 & s2

print s1 | s2

print s1 ^ s2

s1.add((2, 4))
print s1


# -- coding: utf-8 --


#循环遍历时，可以使用enumerate()函数同时检索位置索引和相应的值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

#要同时循环两个或更多个序列，条目可以与该zip()功能配对
questions = ['name', 'quest', 'favorite color']

answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print 'What is your {0}. It is {1}'.format(q, a)


for i in reversed(xrange(1, 11, 3)):
    print i

#按排序顺序循环序列，使用sorted()返回新排序列表的函数，同时保持源不变

abc = set('dagdcfw')

for i in sorted(abc):
    print i

print abc

#循环遍历字典时，可以使用该iteritems()方法同时检索键和对应的值

for k, v in {'name': 'Lancelot', 'quest': 'the holy grail'}.iteritems():
    print k, v

#当循环列表时，有时可能会改变一个列表；创建新列表通常更简单，更安全
import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN')]
filtered_date = []

print raw_data

for value in raw_data:
    if not math.isnan(value):
        filtered_date.append(value)

print filtered_date

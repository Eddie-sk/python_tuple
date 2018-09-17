# -- coding: utf-8 --

#Python还包括集合的数据类型。集合是无序集合，没有重复元素。基本用途包括成员资格测试和消除重复条目。集合对象还支持数学运算，如并集，交集，差异和对称差异。

#大括号或set()函数可用于创建集合。注意：要创建一个空集，你必须使用set()，而不是{}; 后者创建一个空字典，一个我们将在下一节讨论的数据结构。


basket = ['apple', 'orange', 'apple', 'pear', 'banana', 'banana']

fruit = set(basket)

print fruit

print {'apple', 'apple'}, {}


a = set('abcdefg')
b = set('fghijklmn')

print a - b #unique letters in a but not in b

print a ^ b #unique letters in a or b but not both

print a | b #letters in either a or b

print a & b #letters in both a and b

abc = set('abcdefghijk')

c = [x for x in abc if x not in 'def']

print c

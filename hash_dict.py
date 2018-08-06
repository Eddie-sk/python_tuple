# -*- coding:utf-8 -*-
dic = {'zhangsan': 99, 'lisi': 32}
print dic['lisi']
dic['lisi'] = 90
print dic['lisi']
dic['lisi'] = 91
print dic['lisi']
#print dic['lisi1'] key不存在，dic会报错，避免报错有两种方法
#1.通过in判断key是否存在
print 'wangwu' in dic

#2.通过get(),如果key不存在，返回None, 或者自定义返回错误码Value：
print dic.get('wangma')
print dic.get('zhaoliu', 'not found')

#移除某个Key，前提：key存在
dic.pop('lisi')

dic['tuple'] = (1, 2, 3)
print dic

#跟list相比dic的特点：
#1、查找和插入的速度快，不会随着key 的增加而变慢；
#2、需要占用大量内存
#list:
#1、查找和插入的时间随着元素的增加而增加
#2、占用空间小，浪费内存少
#so：dic用空间换取时间


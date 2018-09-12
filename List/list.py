# -- coding: utf-8 --

class person(object):

    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None



arr1 = [1, 23]
arr1.append(123)
arr1.extend([4, 5, 6])
print arr1
arr1.pop()  # 删除列表中给定位置的项目，然后将其返回。如果未指定索引，则删除列表中的最后一项

arr1.count(23)  # 返回列表中'23'出现的次数

arr1.sort(cmp=lambda x, y: cmp(y, x), reverse=1)
print arr1

t = person()
t.name = '张三'
t.age = 10
t.gender = '男'
print t.__getattribute__(t.name)

t2 = person()
t2.name = '李四'
t2.age = 15
t2.gender = '女'

arr2 = [t, t2]

arr2.sort(cmp=lambda x, y: cmp(x.age, y.age), reverse=False)
print arr2
